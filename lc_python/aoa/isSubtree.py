# https://leetcode.com/problems/subtree-of-another-tree/
# Given two non-empty binary trees s and t, check whether tree t has exactly 
# the same structure and node values with a subtree of s. A subtree of s is a 
# tree consists of a node in s and all of this node's descendants. The tree s 
# could also be considered as a subtree of itself.

# Example 1:
#     Given tree s:
#         3
#         / \
#        4   5
#       / \
#      1   2
#     Given tree t:
#      4 
#     / \
#    1   2
#     Return true, because t has the same structure and node values with a subtree of s.
#
# Example 2:
#     Given tree s:
#          3
#         / \
#        4   5
#       / \
#      1   2
#         /
#        0
#     Given tree t:
#      4
#     / \
#    1   2
#     Return false.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self, node):
        if node:
            self.printTree(node.left)
            print(node.val)
            self.printTree(node.right)

class Solution:
    def __init__(self):
        pass
        
    def getTreePathString(self, node):
        if node == None:
            return 'none'
        return '#' + str(node.val) + ' ' + str(self.getTreePathString(node.left)) + ' ' + str(self.getTreePathString(node.right))

    def isSubtree(self, fullTree: TreeNode, subTree: TreeNode) -> bool:
        subTreePath = self.getTreePathString(subTree)
        fullTreePath = self.getTreePathString(fullTree)

        print("subTreePath =", subTreePath)
        print("fullTreePath =", fullTreePath)

        if subTreePath is None or fullTreePath is None:
            return None
        else:
            if subTreePath in fullTreePath:
                return True
            else:
                return False

sol = Solution()
t = TreeNode(3)
t.left = TreeNode(4)
t.left.left = TreeNode(1)
t.left.right = TreeNode(2)
t.right = TreeNode(5)
# t.printTree(t)
s = TreeNode(4)
s.left = TreeNode(1)
s.right = TreeNode(2)
# s.printTree(s)
solution = True
output = sol.isSubtree(t, s)
print("%s | %s" % (output == solution, output))


t = TreeNode(3)
t.left = TreeNode(4)
t.left.left = TreeNode(1)
t.left.right = TreeNode(2)
t.left.right.left = TreeNode(0)
t.right = TreeNode(5)
# t.printTree(t)
s = TreeNode(4)
s.left = TreeNode(1)
s.right = TreeNode(2)
# s.printTree(s)
solution = False
output = sol.isSubtree(t, s)
print("%s | %s" % (output == solution, output))
