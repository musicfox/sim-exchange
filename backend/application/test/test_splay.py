import pytest
import os
import sys

from demand_queue_splay import *

def test_insert():
    o1 = Order(mu=.05, sigma=.10, cash=100, time_stamp=datetime.date.today())
    n1 = Node(o1)
    tree = OrderBook()
    tree.insert(n1)

    assert tree.root.data == 100

def test_search():
    o1 = Order(mu=.05, sigma=.10, cash=100, time_stamp=datetime.date.today())
    o2 = Order(mu=.15, sigma=.20, cash=200, time_stamp=datetime.date.today())
    o3 = Order(mu=.25, sigma=.30, cash=150, time_stamp=datetime.date.today())
    o4 = Order(mu=.25, sigma=.30, cash=50, time_stamp=datetime.date.today())

    n1 = Node(o1)
    n2 = Node(o2)
    n3 = Node(o3)
    n4 = Node(o4)

    tree = OrderBook()

    tree.insert(n1)
    tree.insert(n2)
    tree.insert(n3)
    tree.insert(n4)

    tree.search_tree(n3)

    assert tree.root.data == 150

def test_delete():
    o1 = Order(mu=.05, sigma=.10, cash=100, time_stamp=datetime.date.today())
    n1 = Node(o1)
    tree = OrderBook()
    tree.insert(n1)
    tree.delete_node(n1)

    assert tree.root == None

