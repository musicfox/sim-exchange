"""
The Investor, Artist, and simulation classes.
"""
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
import datetime


@dataclass
class InvestorUser(DataClassJsonMixin):
    """
    # `InvestorUser`

    A dataclass to house and organize an investor's feature information.

    ## Usage
    ```python
    >>> # serialization usage
    >>> Investor.to_json() 
    >>> Investor.to_dict()
    >>> Investor.from_json()
    >>> Investor.from_dict()
    ```
    """

    mu: float
    sigma: float
    principal: float
    remaining_principal: float
    genre: str
    time_horizon: datetime.datetime
    investments: dict


@dataclass
class AssetUser(DataClassJsonMixin):
    """
    # `AssetUser`

    A dataclass to house and organize an artist's feature information.

    ## Usage
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

    mu: float
    sigma: float
    ranking: float
    genre: str
    expiration_date: datetime.datetime
    pricing_date: datetime.datetime
    investors: dict
