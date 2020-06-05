import time, random

from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
import datetime
import pandas as pd
import sys
import pytest

class Order:
    def __init__(self, mu, sigma, data, time_stamp):
        self.mu = mu
        self.sigma = sigma
        self.data = data
        self.time_stamp = time_stamp
        self.parent = None
        self.left = None
        self.right = None

    #Keep for now to look at printed output
    def __str__(self):
        return f'Order(mu= {self.mu} , sigma= {self.sigma}, data= {self.data}, time= {self.time_stamp})'


class OrderBook:  # SplayTree
    def __init__(self):
        self.root = None

    def __delete_order_helper(self, order, key):
        x = None
        t = None
        s = None
        while order != None:
            if order.data == key:
                x = order

            if order.data <= key:
                order = order.right
            else:
                order = order.left

        if x == None:
            print("Couldn't find key in the tree")
            return

        # split operation
        self.__splay(x)
        if x.right != None:
            t = x.right
            t.parent = None
        else:
            t = None

        s = x
        s.right = None
        x = None

        # join operation
        if s.left != None:
            s.left.parent = None

        self.root = self.__join(s.left, t)
        s = None

    """
    Join() and maximum() will assist with deleting nodes.

    """

    # joins two trees s and t
    def __join(self, s, t):
        if s == None:
            return t

        if t == None:
            return s

        x = self.maximum(s)
        self.__splay(x)
        x.right = t
        t.parent = x
        return x

        # find the order with the maximum key

    def maximum(self, order):
        while order.right != None:
            order = order.right
        return order

    """
    ZAG-ROTATION:

    This is similar to a LEFT rotation. Every node moves a position to the left. 
    We can do a zag rotation if a node is a right child of the root node. 

    """

    def __left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    """
    ZIG-ROTATION:

    This is similar to a RIGHT rotation. Every node moves a position to the right. 
    We can do a zig rotation if a node is a left child of the root node. 

    """

    def __right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent;
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    """
    By "splaying" a tree, necessary operations (zig/zag) are performed to bring a node to the root of the tree. 
    """

    # Splaying operation. Move x to the root of the tree
    def __splay(self, x):
        while x.parent != None:
            if x.parent.parent == None:
                if x == x.parent.left:
                    # zig rotation
                    self.__right_rotate(x.parent)
                else:
                    # zag rotation
                    self.__left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # zig-zig rotation
                self.__right_rotate(x.parent.parent)
                self.__right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # zag-zag rotation
                self.__left_rotate(x.parent.parent)
                self.__left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # zig-zag rotation
                self.__left_rotate(x.parent)
                self.__right_rotate(x.parent)
            else:
                # zag-zig rotation
                self.__right_rotate(x.parent)
                self.__left_rotate(x.parent)

    def __search_tree_helper(self, order, key):
        if order == None or key == order.data:
            return order

        if key < order.data:
            return self.__search_tree_helper(order.left, key)
        return self.__search_tree_helper(order.right, key)

    # search the tree for the key k
    # and return the corresponding order
    def search_tree(self, order):
        x = self.__search_tree_helper(self.root, order.data)
        if x != None:
            self.__splay(x)

    # insert the key to the tree in its appropriate position
    def insert(self, order):
#         order = Order
        y = None
        x = self.root

        while x != None:
            y = x
            if order.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        order.parent = y
        if y == None:
            self.root = order
        elif order.data < y.data:
            y.left = order
        else:
            y.right = order
        # splay the node
        self.__splay(order)

    # delete the node from the tree
    def delete_order(self, Order):
        self.__delete_order_helper(self.root, Order.data)
