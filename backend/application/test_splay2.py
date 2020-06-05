import pytest
import os
import sys

from demand_queue_splay2 import *

def test_instance():
    o1 = Order(mu=.05, sigma=.10, data=100, time_stamp=datetime.date.today())

    assert isinstance(o1, Order)

def test_order():
    o1 = Order(mu=.05, sigma=.10, data=100, time_stamp=datetime.date.today())

    assert o1.mu == 0.05

def test_insert():
    o1 = Order(mu=.05, sigma=.10, data=100, time_stamp=datetime.date.today())
    tree = OrderBook()
    tree.insert(o1)

    assert tree.root.data == 100

def test_search():
    o1 = Order(mu=.05, sigma=.10, data=100, time_stamp=datetime.date.today())
    o2 = Order(mu=.15, sigma=.20, data=200, time_stamp=datetime.date.today())
    o3 = Order(mu=.25, sigma=.30, data=150, time_stamp=datetime.date.today())
    o4 = Order(mu=.25, sigma=.30, data=50, time_stamp=datetime.date.today())

    tree = OrderBook()

    tree.insert(o1)
    tree.insert(o2)
    tree.insert(o3)
    tree.insert(o4)

    tree.search_tree(o3)

    assert tree.root.data == 150

def test_delete():
    o1 = Order(mu=.05, sigma=.10, data=100, time_stamp=datetime.date.today())
    tree = OrderBook()
    tree.insert(o1)
    tree.delete_order(o1)

    assert tree.root == None


def test_insert_multiple():
    for i in range(10000):
        o1 = Order(mu=.05, sigma=.10, data=100 + i + 1, time_stamp=datetime.date.today())
        tree = OrderBook()
        tree.insert(o1)

    assert tree.root.data == 10100
