"""
# `conftest.py`

Pytest configuration file including test fixtures and other setup items.

## Usage
```python
python -m pytest -v -d --xt popen//python=python3 # using popen
# boring
python -m pytest -v
# also boring
pytest -v
```
"""
import pytest
import datetime
import random
from entities import InvestorUser, AssetUser


# =============================================================================
# Helper functions.
# =============================================================================
def generateExpiration():
    return datetime.datetime.now() + datetime.timedelta(
        days=random.choice(range(90, 365 * 3))
    )


def generateInvestorUser(genres,):
    """
    # `generateInvestorUser`
    Generate a random investor user.
    """
    rnum = random.random()
    starting_principal = rnum * 10000
    current_principal = starting_principal if rnum < .5 else starting_principal * random.random()
    return InvestorUser(
        mu=random.random(),
        sigma=random.random(),
        principal=starting_principal,
        remaining_principal=current_principal,
        genre=random.choice(genres),
        time_horizon=generateExpiration(),
        investments=dict(),
    )


def generateAssetUser(genres,):
    """
    # `generateAssetUser`
    Generate a random asset user.
    """
    return AssetUser(
        mu=random.random(),
        sigma=random.random(),
        ranking=random.random(),
        genre=random.choice(genres),
        expiration_date=generateExpiration(),
        pricing_date=datetime.datetime.now(),
        investors=dict(),
    )  # TODO Return a simulated artist user.


# =============================================================================
# Reusable test fixtures.
# =============================================================================
@pytest.fixture(scope="module")
def contributors():
    # TODO Scrape README.md for names
    return [
        "@sssyzz",
        "@RKoulikova",
        "@yzhao0429",
        "@sebastientradair",
        "@philipmuh",
        "@Zhrong25",
        "@thinkjrs",
    ]


@pytest.fixture(scope="module")
def genres():
    """
    # `genres`
    Return the available genres set statically.
    """
    return [
        "pop",
        "hip hop",
        "country",
        "rock",
    ]


@pytest.fixture(scope="module")
def expiration_date():
    return generateExpiration()


@pytest.fixture(scope="module")
def investor_user(genres,):  
    """
    # `investor_user`
    Pytest fixture to generate a random investor user.

    """
    return generateInvestorUser(genres)


@pytest.fixture(scope="module")
def asset_user(genres,):  
    """
    # `artist_user`
    A pytest fixture to generate a random investor user.
    """
    return generateAssetUser(genres)


@pytest.fixture(scope="module")
def investorUsers(genres):  
    """
    # `investorUsers`
    A pytest fixture to return a generator of randomly generated
    investor users.
    """
    return [generateInvestorUser(genres) for i in range(1000)]


@pytest.fixture(scope="module")
def assetUsers(genres):  
    """
    # `assetUsers`
    A pytest fixture to return a generator of randomly generated
    asset users.
    """
    return [generateAssetUser(genres) for i in range(1000)]


@pytest.fixture(scope="module")
def startValArrivalPath():
    return 20


@pytest.fixture(scope="module")
def arrivalPath(startValArrivalPath):  
    """
    # `arrivalPath`
    A pytest fixture to return a simulated user arrival path based on
    past wikipedia data for major actors/actresses.
    """
    from datasets import userArrivals

    # first set an arbitrary starter
    userArrivals.loc[userArrivals.index[0], "chg"] = startValArrivalPath
    userArrivals["arrivals"] = (
        userArrivals[["chg"]].cumsum().round()
    )  # generate an arrival path based on the wikipedia data of actors
    return userArrivals[["arrivals"]]
