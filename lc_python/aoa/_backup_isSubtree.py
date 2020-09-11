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

    def insertNode(self, node, value):
        if node is None:
            return TreeNode(value)
        else:
            if node.val == value:
                return node
            elif node.val < value:
                node.right = self.insertNode(node.right, value)
            else:
                node.left = self.insertNode(node.left, value)
        return node

    def printTree(self, node):
        if node:
            self.printTree(node.left)
            print(node.val)
            self.printTree(node.right)

class Solution:
    def __init__(self):
        pass
        # subTreePath = []
        # fullTreePath = []

    def getTreePath(self, node):
        if node is None:
            return None
        leftTree = self.getTreePath(node.left)
        rightTree = self.getTreePath(node.right)

        nodeList = []
        nodeList.append(node.val)
        if leftTree:
            for item in leftTree:
                nodeList.append(item)
        if rightTree:
            for item in rightTree:
                nodeList.append(item)
        return nodeList
        
    def getTreePathString(self, node):
        if node == None:
            return 'none'
        # leftTree = self.getTreePathString(node.left)
        # rightTree = self.getTreePathString(node.right)
        return '#' + str(node.val) + ' ' + str(self.getTreePathString(node.left)) + ' ' + str(self.getTreePathString(node.right))

    def isSubtree(self, subTree: TreeNode, fullTree: TreeNode) -> bool:

        # get path of subtree
        # stackList = []
        # visited = []
        # subTreePath = []
        # Fail #1
        # stackList.append(subTree)
        # while stackList:
        #     currentNode = stackList.pop()
        #     subTreePath.append(currentNode.val)
            
        #     if currentNode not in visited:
        #         visited.append(currentNode)
            
        #     if currentNode.left and currentNode.left not in visited:
        #         stackList.append(currentNode.left)
        #     if currentNode.right and currentNode.right not in visited:
        #         stackList.append(currentNode.right)
        
        # Fail #2
        # currentNode = subTree
        # while True:
        #     if currentNode:
        #         subTreePath.append(currentNode.val)
        #         stackList.append(currentNode)
        #         currentNode = currentNode.left
        #     elif (stackList):
        #         currentNode = stackList.pop()
        #         currentNode = currentNode.right
        #     else:
        #         break

        # Fail #3
        # subTreePath = self.getTreePath(subTree)
        
        # Fail #4 - BFS
        # get path of subtree
        # stackList = []
        # visited = []
        # subTreePath = []
        # stackList.append(subTree)
        # while stackList:
        #     currentNode = stackList.pop(0)
        #     subTreePath.append(currentNode.val)

        #     if currentNode not in visited:
        #         visited.append(currentNode)

        #     if currentNode.left and currentNode.left not in visited:
        #         stackList.append(currentNode.left)
        #     if currentNode.right and currentNode.right not in visited:
        #         stackList.append(currentNode.right)

        # Fail #5
        subTreePath = self.getTreePathString(subTree)
        
        
        

        # get path of fulltree
        # stackList = []
        # visited = []
        # fullTreePath = []
        # Fail #1
        # stackList.append(fullTree)
        # while stackList:
        #     currentNode = stackList.pop()
        #     fullTreePath.append(currentNode.val)

        #     if currentNode not in visited:
        #         visited.append(currentNode)

        #     if currentNode.left and currentNode.left not in visited:
        #         stackList.append(currentNode.left)
        #     if currentNode.right and currentNode.right not in visited:
        #         stackList.append(currentNode.right)

        # Fail #2
        # currentNode = fullTree
        # while True:
        #     if currentNode:
        #         fullTreePath.append(currentNode.val)
        #         stackList.append(currentNode)
        #         currentNode = currentNode.left
        #     elif (stackList):
        #         currentNode = stackList.pop()
        #         currentNode = currentNode.right
        #     else:
        #         break

        # Fail #3
        # fullTreePath = self.getTreePath(fullTree)

        # Fail #4 - BFS
        # get path of fulltree
        # stackList = []
        # visited = []
        # fullTreePath = []
        # stackList.append(fullTree)
        # while stackList:
        #     currentNode = stackList.pop()
        #     fullTreePath.append(currentNode.val)

        #     if currentNode not in visited:
        #         visited.append(currentNode)

        #     if currentNode.left and currentNode.left not in visited:
        #         stackList.append(currentNode.left)
        #     if currentNode.right and currentNode.right not in visited:
        #         stackList.append(currentNode.right)

        # Fail #5
        fullTreePath = self.getTreePathString(fullTree)

        # Fail #6
        # return self.traverse(subTree, fullTree)

        print(subTreePath)
        print(fullTreePath)

        if subTreePath is None or fullTreePath is None:
            return None
        else:
            if subTreePath in fullTreePath:
                return True
            else:
                return False
            # result = set(x in fullTreePath for x in subTreePath)
            # if result:
            #     return True
            # else:
            #     return False


    def traverse(self, s, t):
        return s != None and ( self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))
        
    def equals(self, x, y):
        if x == None and y == None:
            return True
        if x == None or y == None:
            return False
        return x.val == y.val and self.equals(x.left, y.left) and self.equals(x.right, y.right)

sol = Solution()
t = TreeNode(3)
# t.insertNode(t, 4)
# t.insertNode(t, 5)
# t.insertNode(t, 1)
# t.insertNode(t, 2)
t.left = TreeNode(4)
t.left.left = TreeNode(1)
t.left.right = TreeNode(2)
t.right = TreeNode(5)
# t.printTree(t)
s = TreeNode(4)
# s.insertNode(s, 1)
# s.insertNode(s, 2)
s.left = TreeNode(1)
s.right = TreeNode(2)
solution = True
output = sol.isSubtree(s, t)
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
# t.printTree(s)
solution = False
output = sol.isSubtree(s, t)
print("%s | %s" % (output == solution, output))
