import pandas as pd
import os


userArrivals = pd.read_csv(
    os.path.join(os.path.abspath(__file__).strip('__init__.py'), 'arrivals_wikipedia.csv'),
)
userArrivals.index = userArrivals['Unnamed: 0']
del userArrivals['Unnamed: 0']
print(userArrivals.head())