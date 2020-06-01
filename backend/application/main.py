import scipy
import numpy as np
import random
import pandas as pd
from datetime import datetime

from OPL import OPL
from Users import Artist, Investor


def generateData(num, mean_min, mean_max):
    A = scipy.random.rand(num, num)  # uniform distribution between 0 and 1
    cov_mat = np.dot(A, A.transpose())
    # generate num**2 observations
    rv = np.random.multivariate_normal([random.randint(mean_min, mean_max) / float(100) for x in range(num)], cov_mat,
                                       num ** 2)
    ts_now = datetime.now().timestamp()
    timestamps = [ts_now - x * 60 * 60 * 24 * 30 for x in range(num ** 2 - 1, -1, -1)]
    datetimes = [datetime.strftime(datetime.fromtimestamp(x), "%Y-%m") for x in timestamps]
    history = pd.DataFrame(rv, index=datetimes)
    history.index.name = 'date'
    return history

if __name__ == '__main__':
    print("hi")
    history = generateData(10, 5, 50)
    artists = []
    genres = ["rnb", "country", "disco", "pop"]
    artists = [Artist(pd.DataFrame({'income':history[i].values}).set_index(history.index), random.choice(genres), random.randint(3, 18), random.randint(10, 100)*100) for i in range(10)]
    for i in range(len(artists)):
        print(i, artists[i].mu)
        print(i, artists[i].sigma)
        print(i, artists[i].expiration_date)
    # ignore the sigma from investors for now
    investors = [Investor(random.randint(5, 50)/float(100), 1, random.choice(genres), random.randint(3, 18), random.randint(10, 100)*100) for i in range(10) for i in range(10)]
    print(investors[8].genre)
    print(investors[8].genre)
    print(investors[9].principal)
    print(investors[9].principal)

    opl = OPL()
    opl.add_artists(artists)  # from dealer
    opl.add_investors(investors)  # from dealer

    print(len(opl.artist_filled))
    print(len(opl.investor_filled))

