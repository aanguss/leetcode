# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3525/
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
#
# Given the root of a binary tree, find the maximum value V for which there exist 
# different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
#
# A node A is an ancestor of B if either: any child of A is equal to B, or any 
# child of A is an ancestor of B.
#
# Example 1:
#                       8
#                     /   \
#                   3       10
#                 /   \       \
#                1     6       14
#                     / \      /
#                    4   7    13
#
#     Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
#     Output: 7
#     Explanation: We have various ancestor-node differences, some of which are given below :
#     |8 - 3| = 5
#     |3 - 7| = 4
#     |8 - 1| = 7
#     |10 - 13| = 3
#     Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
# Example 2:
#                     1
#                      \
#                       2
#                        \
#                         0
#                        /
#                       3
#
#     Input: root = [1,null,2,null,0,3]
#     Output: 3
# Constraints:
#     The number of nodes in the tree is in the range [2, 5000].
#     0 <= Node.val <= 105
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # https://www.geeksforgeeks.org/iterative-depth-first-traversal/
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0

        # go through all nodes DFS stack
        binaryStack = []
        binaryDict = {}
        maxDifference = 0

        binaryStack.append(root)
        while len(binaryStack) != 0:
            decendStack = []
            currentNode = binaryStack.pop()
            binaryDict[currentNode.val] = []
            decendStack.append(currentNode)
            while len(decendStack) != 0:
                node = decendStack.pop()
                # print(currentNode.val, node.val)
                # binaryDict[currentNode.val].append(node.val)
                binaryDict[currentNode.val].append(abs(currentNode.val-node.val))
                if abs(currentNode.val - node.val) > maxDifference:
                    maxDifference = abs(currentNode.val - node.val)
                if node.left != None:
                    decendStack.append(node.left)
                if node.right != None:
                    decendStack.append(node.right)
            if currentNode.left != None:
                binaryStack.append(currentNode.left)
            if currentNode.right != None:
                binaryStack.append(currentNode.right)
                
        # print(binaryDict)
        return maxDifference

s = Solution()
#                       8
#                     /   \
#                   3       10
#                 /   \       \
#                1     6       14
#                     / \      /
#                    4   7    13
t1 = TreeNode(8)
t1.left = TreeNode(3)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(6)
t1.left.right.left = TreeNode(4)
t1.left.right.right = TreeNode(7)
t1.right = TreeNode(10)
t1.right.right = TreeNode(14)
t1.right.right.left = TreeNode(13)
solution = 7
output = s.maxAncestorDiff(t1)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

#                     1
#                      \
#                       2
#                        \
#                         0
#                        /
#                       3
t2 = TreeNode(1)
t2.right = TreeNode(2)
t2.right.right = TreeNode(0)
t2.right.right.left = TreeNode(3)
solution = 3
output = s.maxAncestorDiff(t2)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

#                     1

t3 = TreeNode(1)
solution = 0
output = s.maxAncestorDiff(t3)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))
