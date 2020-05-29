import datetime
import pandas as pd

class TooMuchFundError(Exception):
    print("Do not need that much money!")

class TooLittlePrincipalError(Exception):
    print("Need more than that much money!")

class OverInvestError(Exception):
    print("I did not wanna spend that much")

class Artist:

    '''
    mu: float
    sigma: float
    ranking: float
    genre: str
    expiration_date: datetime.datetime
    pricing_date: datetime.datetime
    investors: dict
    history: pandas.DataFrame # need history of mu to generate covariance for MV-analysis
    total_fund: float
    remaining_fund: float
    id: int
    '''

    '''
    history: dataframe of history earning of similiar projects of this artist. index = "date", columns = "income"
    genre: string of genre name, 4 kinds in total
    horizon: number of month before that this project is expected to pay back
    '''
    artist_id_traker = 0

    def __init__(self, history, genre, horizon, total_fund):
        self.history = history
        self.mu = history["income"].mean()
        self.sigma = history["income"].std(ddof = 1)
        self.genre = genre
        self.expiration_date = datetime.today() + pd.offsets.DateOffset(months=horizon)
        self.pricing_date = datetime.today()
        self.investors = []
        self.total_fund = total_fund
        self.remaining_fund = total_fund
        global artist_id_traker
        self.id = artist_id_traker
        artist_id_traker += 1

    '''
    if return 1, then need to delete the artist from queue
    '''
    def update_remaining_fund(self, investor_id, deduction):
        if (deduction > self.remaining_fund):
            raise TooMuchFundError
        self.remaining_fund -= deduction
        self.investors.append(investor_id)
        if self.remaining_fund == 0:
            return 1
        return 0


class Investor:

    '''
    mostly self-explanatory and similiar to above
    '''

    investor_id_traker = 0

    def __init__(self, mu, sigma, genre, horizon, principal):
        if principal < 30:
            raise TooLittlePrincipalError;
        self.mu = mu
        self.sigma = sigma
        self.genre = genre
        self.expiration_date = datetime.today() + pd.offsets.DateOffset(months=horizon)
        self.principal = principal
        self.remaining_principal = principal
        self.artists = []
        global investor_id_traker
        self.id = investor_id_traker
        investor_id_traker += 1

    '''
    if return 1, then need to delete the investor from queue
    '''
    def update_remaining_principal(self, artist_id, deduction):
        if (deduction > self.remaining_fund):
            raise OverInvestError
        self.remaining_fund -= deduction
        self.investors.append(artist_id)
        if self.remaining_fund == 0:
            return 1
        return 0







