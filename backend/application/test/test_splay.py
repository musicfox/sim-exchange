import os
import sys
import random
import datetime
import pytest
import time

from demand_queue_splay import Order, Node, OrderBook


@pytest.fixture(scope="module")
def testOrderData():
    return dict(
        mu=random.random(),
        sigma=random.random(),
        cash=random.random() * 100,
        time_stamp=datetime.datetime.today(),
    )


@pytest.fixture(scope="module")
def testOrder(testOrderData):
    return Order(**testOrderData)


@pytest.fixture(scope="module")
def testNode(testOrder):
    return Node(testOrder)


def test_Order(testOrder, testOrderData):
    # test creation
    assert isinstance(testOrder, Order)

    # make another one
    o1 = Order(**testOrderData)
    # checking parameters
    assert o1.mu == testOrder.mu
    assert o1.sigma == testOrder.sigma
    assert o1.cash == testOrder.cash
    assert o1.time_stamp == testOrder.time_stamp

    # test print
    assert "sigma" in str(testOrder)


def test_Node(testNode, testOrder):
    # test creation
    assert isinstance(testNode, Node)

    # check params
    n1 = Node(testOrder)

    for p1, p2 in zip(testNode.__dict__.items(), n1.__dict__.items()):
        # check parameter names
        assert p1[0] == p2[0]
        # check values
        assert p1[1] == p2[1]


def test_OrderBook_insert():
    o1 = Order(mu=0.05, sigma=0.10, cash=100, time_stamp=datetime.date.today())
    n1 = Node(o1)
    tree = OrderBook()
    tree.insert(n1)

    assert tree.root.data == 100


def test_OrderBook_search():
    o1 = Order(mu=0.05, sigma=0.10, cash=100, time_stamp=datetime.date.today())
    o2 = Order(mu=0.15, sigma=0.20, cash=200, time_stamp=datetime.date.today())
    o3 = Order(mu=0.25, sigma=0.30, cash=150, time_stamp=datetime.date.today())
    o4 = Order(mu=0.25, sigma=0.30, cash=50, time_stamp=datetime.date.today())

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


def test_OrderBook_delete():
    o1 = Order(mu=0.05, sigma=0.10, cash=100, time_stamp=datetime.date.today())
    n1 = Node(o1)
    tree = OrderBook()
    tree.insert(n1)
    tree.delete_node(n1)

    assert tree.root == None


def test_OrderBook_many_iters(testNode, investorUsers):
    """
    This test helps ensure that the tree itself, datastructure-wise, is working correctly. The below
    uses small-scale simulation to ensure that things take relatively appropriate amounts of time to
    execute.
    """
    tree = OrderBook()
    opl_nodes = []
    for user in investorUsers:
        n = Node(
            Order(
                mu=user.mu,
                sigma=user.sigma,
                cash=user.principal,
                time_stamp=datetime.datetime.today(),
            )
        )
        opl_nodes.append(n)
        tree.insert(n)

    # get a random user and search for that user repeatedly, timing it
    usr = random.choice(opl_nodes)
    start1 = time.time()
    for i in range(500):
        # simulate "random" call
        random.choice(opl_nodes)
        tree.search_tree(usr)
    t1_len = time.time() - start1

    start2 = time.time()
    for i in range(500):
        # use random to call actual separate items
        tree.search_tree(random.choice(opl_nodes))
    t2_len = time.time() - start2

    # the first should be much faster if splaying correctly
    assert t1_len < t2_len
