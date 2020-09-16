#!/usr/bin/python3

from typing import List


class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def findNode(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.findNode(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.findNode(value)
        else:
            return self.value

    def insertNode(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insertNode(value)
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insertNode(value)
        else:
            self.value = value

    def deleteNode(self, value):
        # if self.value == value:
        #     if self.right and self.left:
        #         # get the successor node and its parent
        #         [psucc, succ] = self.right._findMin(self)

        #         # splice out the successor
        #         # (we need the parent to do this)

        #         if psucc.left == succ:
        #             psucc.left = succ.right
        #         else:
        #             psucc.right = succ.right

        #         # reset the left and right children of the successor

        #         succ.left = self.left
        #         succ.right = self.right

        #         return succ
        #     else:
        #         if self.right:
        #             return self.right
        #         else:
        #             return self.left
        # else:
        #     if self.value > value:
        #         if self.left:
        #             self.left = self.left.deleteNode(value)
        #     else:
        #         if self.right:
        #             self.right = self.right.deleteNode(value)
        # return self

    def printTree(self):
        # print("\n")
        if self.left:
            self.left.printTree()
            print('\n')
        print(self.value, end=' ')
        if self.right:
            self.right.printTree()
            print('\n')
    

t = TreeNode(12)
t.insertNode(6)
t.insertNode(14)
t.insertNode(3)
t.insertNode(7)
# t.insertNode(1)
t.printTree()

t.deleteNode(14)
t.printTree()
