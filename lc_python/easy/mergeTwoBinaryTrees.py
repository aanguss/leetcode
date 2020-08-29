# https://leetcode.com/problems/merge-two-binary-trees/
# 617. Merge Two Binary Trees
# Easy
# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
# Example 1:
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
# Note: The merging process must start from the root nodes of both trees.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _printTreeDepth(self, tree: TreeNode):
        if tree.val:
            print(tree.val)
        if(tree.left):
            print("l:", end='')
            self._printTreeDepth(tree.left)
        if(tree.right):
            print("r:", end='')
            self._printTreeDepth(tree.right)

    def _printTreeBreadth(self, tree: TreeNode):
        queue = []
        currentList = []
        level = 1
        current = tree
        queue.append([0, "r", current])
        currentList = queue.pop(0)
        while(currentList):
            # print(f"{currentList[0]}:{currentList[1]}-{currentList[2].val}")
            print(f"level {currentList[0]} - {currentList[2].val}")
            if (currentList[2].left):
                queue.append([level, 'l', currentList[2].left])
            if (currentList[2].right):
                queue.append([level, 'r', currentList[2].right])
            level += 1
            if not queue:
                break
            else:
                currentList = queue.pop(0)
    
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if (t1 and t2):
            newTree = TreeNode(t1.val + t2.val)
            newTree.left = self.mergeTrees(t1.left, t2.left)
            newTree.right = self.mergeTrees(t1.right, t2.right)
        elif (t1):
            newTree = TreeNode(t1.val)
            newTree.left = self.mergeTrees(t1.left, None)
            newTree.right = self.mergeTrees(t1.right, None)
        elif (t2):
            newTree = TreeNode(t2.val)
            newTree.left = self.mergeTrees(None, t2.left)
            newTree.right = self.mergeTrees(None, t2.right)
        else:
            return None
        
        # if (t1 and t2 and t1.left and t2.left):
        #     newTree.left = self.mergeTrees(t1.left, t2.left)
        # elif (t1 and t1.left):
        #     newTree.left = self.mergeTrees(t1.left, None)
        # elif (t2 and t2.left):
        #     newTree.left = self.mergeTrees(None, t2.left)

        # if (t1 and t2 and t1.right and t2.right):
        #     newTree.right = self.mergeTrees(t1.right, t2.right)
        # elif (t1 and t1.right):
        #     newTree.right = self.mergeTrees(t1.right, None)
        # elif (t2 and t2.right):
        #     newTree.right = self.mergeTrees(None, t2.right)

        return newTree

    def mergeTreesTiny(self, t1: TreeNode, t2: TreeNode):
        if None in (t1, t2):
            return t1 or t2
        t1.val += t2.val
        t1.left = self.mergeTreesTiny(t1.left, t2.left)
        t1.right = self.mergeTreesTiny(t1.right, t2.right)
        return t1

s = Solution()

tree1 = TreeNode(1)
tree1.left = TreeNode(3)
tree1.right = TreeNode(2)
tree1.left.left = TreeNode(5)
print("tree1-dfs")
s._printTreeDepth(tree1)
print("tree1-bfs")
s._printTreeBreadth(tree1)

tree2 = TreeNode(2)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)
tree2.left.right = TreeNode(4)
tree2.right.right = TreeNode(7)
tree2.right.left = TreeNode(1)
print("tree2-dfs")
s._printTreeDepth(tree2)
print("tree2-bfs")
s._printTreeBreadth(tree2)

newTree = TreeNode()
newTree = s.mergeTrees(tree1, tree2)
print("newTree-dfs")
s._printTreeDepth(newTree)
print("newTree-bfs")
s._printTreeBreadth(newTree)

newTreeTiny = TreeNode()
newTreeTiny = s.mergeTreesTiny(tree1, tree2)
print("newTreeTiny-dfs")
s._printTreeDepth(newTreeTiny)
print("newTreeTiny-bfs")
s._printTreeBreadth(newTreeTiny)