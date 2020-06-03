import threading
import numpy as np
from collections import deque
import pandas as pd
from scipy.optimize import minimize

class BadOptimizationError(Exception):
    def __init__(self, msg):
        self.value = msg

    def __str__(self):
        return (repr(self.value))

lock = threading.Lock()
genre_dict = {0: "country", 1: "electronic", 2: "rnb", 3: "rock"}

'''
sample implementation:
opl = OPL()
opl.add_artists(artists) # from dealer
opl.add_investors(investors) # from dealer
need to add functions for communications
'''
class OPL(threading.Thread):
    def __init__(self):
        # first create a hash map for "best" artists
        top_deal = {} # a dict of smallest sigma w.r.t specific mu
        for i in np.arange(0.0, 100.0, 0.1):
            key = self.floatToStr(i)
            top_deal[key] = None
        self.top_deal = top_deal
        # assume the efficient frontier is reasonable
        self.sigma_min = float("inf")
        self.sigma_min_pos = 0
        self.artist_filled = []
        self.investor_filled = []
        self.artist_queue = []
        self.investor_queue = deque()

    '''
    artists: a list of Artist, sent from dealer class
    '''
    def add_artists(self, artists):
        self.artist_queue += artists
        for art in artists:
            key = self.floatToStr(art.mu)
            if self.top_deal[key] == None:
                self.top_deal[key] = art
                if art.sigma < self.sigma_min:
                    self.sigma_min_pos = art.mu
            elif art.sigma < self.top_deal[key].sigma:
                self.top_deal[key] = art
                if art.sigma < self.sigma_min:
                    self.sigma_min_pos = art.mu
        self.createMatches()

    '''
    investors: a list of Investors, sent from dealer class
    '''
    def add_investors(self, investors):
        for inv in investors:
            if self.matchOne(inv) == 1:
                self.investor_filled.append(inv)
            else:
                # because shallow copy
                self.investor_queue.append(inv)

    def floatToStr(self, num):
        exp = str(num).split(".")
        if len(exp) > 1:
            key = exp[0] + "." + exp[1][0]
        else:
            key = exp[0] + ".0"
        return key
    '''
    Match for this specific investor, return 1 if no remaining fund after matching
    '''
    def matchOne(self, investor):
        if len(self.artist_queue) == 0:
            return 0
        merged = pd.DataFrame()
        last_sigma = 0
        total_fund = 0
        artists_tmp = []
        constraits = []
        for i in np.arange(0.0, 100.0, 0.1):
            # noise cancelling: exclude ones' mu does not increase with sigma
            key = self.floatToStr(i)
            if (self.top_deal[key] == None):
                continue
            if (self.top_deal[key].sigma - last_sigma > 0):
                merged = merged.merge(self.top_deal[key].history, left_index=True, right_index=True, how = "outer")
                lock.acquire()
                total_fund += self.top_deal[key].remaining_fund
                lock.release()
                artists_tmp.append(self.top_deal[key])
                constraits.append(self.top_deal[key].remaining_fund/investor.remaining_principal)

        # disregard genre for now, MV optimize over top deals
        corr_mat = merged.cov().values
        N = len(artists_tmp)
        start_pos = [1 / N for x in range(N)]
        # 1 - sum(x) = 0; constraits > x
        cons = ({'type': 'eq', 'fun': lambda x: 1 - sum(x)}, {'type': 'ineq', 'fun': lambda x: constraits - x})
        bnds = tuple((0, 1) for x in start_pos)
        sigmaFunc = lambda x: x @ corr_mat @ x
        res = minimize(sigmaFunc, start_pos, method='SLSQP', bounds=bnds, constraints=cons)
        result = res.x
        for i in range(N):
            if (result[i] < 0 or result[i] > 1 or round(result[i], 5) > round(constraits[i], 5)): # limit to 5 digites is arbitrary
                raise BadOptimizationError("The minimization returned unwanted result!")
            if abs(result[i] - constraits[i]) < 10**-5:
                # then mark the artist as filled
                artists_tmp[i].remaining_fund = 0
                self.artist_filled.append(artists_tmp[i])
                self.artist_queue.remove(artists_tmp[i])
                key = self.floatToStr(artists_tmp[i].mu)
                self.top_deal[key] = None
                lock.acquire()
                investor.remaining_principal -= artists_tmp[i].remaining_fund
                lock.release()
            else:
                # because shallow copy
                lock.acquire()
                artists_tmp[i].remaining_fund -= result[i] * investor.remaining_principal
                investor.remaining_principal -= artists_tmp[i].remaining_fund
                lock.release()
        self.getNewTopDeal();
        if (investor.remaining_principal/investor.principal) < 0.01:
            # if so, consider the investor as fully filled
            return 1
        else:
            return 0


    '''
    Iterate over all investors in deque
    '''
    def createMatches(self):
        if len(self.investor_queue) == 0:
            return
        for i in range(len(self.investor_queue)):
            head = self.investor_queue.popleft()
            inv_tmp = self.matchOne(head)
            if inv_tmp == None:
                head.remaining_principal = 0
                self.investor_filled.append(head)
            else:
                self.investor_queue.append(inv_tmp)


    def getNewTopDeal(self):
        for art in self.artist_queue:
            key = self.floatToStr(art.mu)
            if self.top_deal[key] == None:
                self.top_deal[key] = art
            elif art.sigma < self.top_deal[key].sigma:
                self.top_deal[key] = art



