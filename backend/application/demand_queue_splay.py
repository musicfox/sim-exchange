from decimal import *
import time, random

import datetime
import pandas as pd
import sys

class Order:
    def __init__(self, mu, sigma, cash, time_stamp):
        self.mu = mu
        self.sigma = sigma
        self.cash = cash
        self.time_stamp = time_stamp

    def __str__(self):
        return 'Order(mu=' + str(self.mu) + ', sigma=' + str(self.sigma) + ', cash=' + str(self.cash) + ', time=' + str(
            self.time_stamp) + ')'

class Node:
    def  __init__(self, order):
        self.data = order.cash
        self.order = order.__str__()
        self.parent = None
        self.left = None
        self.right = None


class OrderBook:  # SplayTree
    def __init__(self):
        self.root = None

    def __delete_node_helper(self, node, key):
        x = None
        t = None
        s = None
        while node != None:
            if node.data == key:
                x = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

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

        # find the node with the maximum key

    def maximum(self, node):
        while node.right != None:
            node = node.right
        return node

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

    def __search_tree_helper(self, node, key):
        if node == None or key == node.data:
            return node

        if key < node.data:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)

    # search the tree for the key k
    # and return the corresponding node
    def search_tree(self, Node):
        x = self.__search_tree_helper(self.root, Node.data)
        if x != None:
            self.__splay(x)

    # insert the key to the tree in its appropriate position
    def insert(self, Node):
        node = Node
        y = None
        x = self.root

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        # splay the node
        self.__splay(node)

    # delete the node from the tree
    def delete_node(self, Node):
        self.__delete_node_helper(self.root, Node.data)
