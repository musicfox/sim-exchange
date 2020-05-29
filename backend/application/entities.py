"""
The Investor, Artist, and simulation classes.
"""
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
import datetime


@dataclass
class InvestorUser(DataClassJsonMixin):
    """
    `InvestorUser`

    A dataclass to house and organize an investor's feature information.

    **Usage**

    ```python
    >>> # serialization usage
    >>> Investor.to_json() 
    >>> Investor.to_dict()
    >>> Investor.from_json()
    >>> Investor.from_dict()
    ```
    """

    mu: float  # given by the incoming user
    sigma: float  # given by the incoming user
    principal: float  # given by the incoming user
    remaining_principal: float  # given by currently allocated less principal
    genre: str  # given by the incoming user
    time_horizon: datetime.datetime  # given by the incoming user
    investments: dict  # store cash flow matches as they're found


@dataclass
class AssetUser(DataClassJsonMixin):
    """
    `AssetUser`

    A dataclass to house and organize an artist's feature information.

    **Usage**

    ```python
    >>> # instantiation
    >>> Artist(mu=.05, sigma=.10, ranking=.33, genre='country', expiration_date=(datetime.today() - pd.offsets.DateOffset(months=6)), pricing_date=datetime.today())
    >>> # serialization usage
    >>> Artist.to_json() 
    >>> Artist.to_dict()
    >>> Artist.from_json()
    >>> Artist.from_dict()
    ```
    """

    mu: float  # given by the incoming user
    sigma: float  # given by the incoming user
    ranking: float  # calculated by the MatchingAlgo
    genre: str  # given by our clustering algorithms
    expiration_date: datetime.datetime  # given by the user
    pricing_date: datetime.datetime  # given by the frontend
    investors: dict  # store cash flow matches as they're found
