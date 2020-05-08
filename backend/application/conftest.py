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


@pytest.fixture(scope='module')
def contributors():
    # TODO Scrape README.md for names
    return [
        '@sssyzz',
        '@RKoulikova', 
        '@yzhao0429',
        '@sebastientradair',
        '@philipmuh',
        '@Zhrong25', 
    ]

@pytest.fixture(scope='module')
def investor_user(): # TODO Implement investor_user
    pass # return a simulated investor user

@pytest.fixture(scope='module')
def artist_user(): # TODO Implement artist_user
    pass # return a simulated artist user

@pytest.fixture(scope='module')
def investorUsers(): # TODO Implement investorUsers
    pass #yield an iterable of generated investor users

@pytest.fixture(scope='module')
def assetUsers(): # TODO IMplement assetUsers
    pass #yield an iterable of generated asset users

@pytest.fixture(scope='module')
def arrivalPath(): # TODO Implement arrivalPath
    pass # generate an arrival path based on the wikipedia data of actors