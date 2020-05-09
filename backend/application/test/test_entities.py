"""
# `test_entities.py`
Unit tests for some common datastructures in `sim-exchange`.
"""
import pytest
from entities import (
    InvestorUser,
    AssetUser,
)
import datetime
import dataclasses


def test_AssetUser(asset_user):
    # instantiation
    assert isinstance(asset_user, AssetUser)
    # extant values
    assert isinstance(asset_user.mu, float)
    assert isinstance(asset_user.sigma, float)
    assert isinstance(asset_user.ranking, float)
    assert isinstance(asset_user.genre, str)
    assert isinstance(asset_user.expiration_date, datetime.datetime)
    assert isinstance(asset_user.pricing_date, datetime.datetime)
    assert isinstance(asset_user.investors, dict)
    
    # data modification
    testSig = asset_user.sigma
    asset_user.sigma = .09 if .09 != testSig else .10
    assert testSig != asset_user.sigma
    # data removal
    asset_user.sigma = None
    assert not dataclasses.asdict(asset_user)['sigma']   

def test_InvestorUser(investor_user):
    # instantiation
    assert isinstance(investor_user, InvestorUser)
    # extant values
    assert isinstance(investor_user.mu, float)
    assert isinstance(investor_user.sigma, float)
    assert isinstance(investor_user.principal, float)
    assert isinstance(investor_user.genre, str)
    assert isinstance(investor_user.time_horizon, datetime.datetime)
    assert isinstance(investor_user.investments, dict)
    
    # data modification
    testSig = investor_user.sigma
    investor_user.sigma = .09 if .09 != testSig else .10
    assert testSig != investor_user.sigma
    # data removal
    investor_user.sigma = None
    assert not dataclasses.asdict(investor_user)['sigma']   

def test_user_generation(assetUsers, investorUsers):
    assert isinstance(assetUsers, list)
    assert isinstance(investorUsers, list)
    assert len(assetUsers)
    assert len(investorUsers)