import pytest
import os
import app as app
from bs4 import BeautifulSoup
import requests

@pytest.fixture
def client():
    # set the application to TESTING
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

@pytest.fixture
def scrape(client):
    """
    Return the Beautiful Soup object
    """
    # get it
    html = client.get('/').data
    # scrape the site with bs4
    soup = BeautifulSoup(html, 'html.parser')
    return soup

@pytest.fixture
def login_payload():
    return dict(email='jason@musicfox.io', password="testing123")

@pytest.fixture
def login_headers():
    return {'User-Agent': 'Musicfox-Corp-test-request-bot'}

def test_index_page(client, scrape, login_headers):
    assert client.get('/').status_code == 200
    assert client.get('/').charset == 'utf-8'
    for a in scrape.find_all('a', href=True):
        if 'https' in a['href']:
            time.sleep(.5)
            assert requests.get(a['href'], headers = login_headers).ok
