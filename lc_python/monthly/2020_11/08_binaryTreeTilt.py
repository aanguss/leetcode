# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3524/
# https://leetcode.com/problems/binary-tree-tilt/
#
# Given the root of a binary tree, return the sum of every tree node's tilt.
#
# The tilt of a tree node is the absolute difference between the sum of all left 
# subtree node values and all right subtree node values. If a node does not have 
# a left child, then the sum of the left subtree node values is treated as 0. 
# The rule is similar if there the node does not have a right child.
#
# Example 1:
#                 1                1
#                / \      --->    / \
#               2   3            0   0
#
#     Input: root = [1,2,3]
#     Output: 1
#     Explanation: 
#     Tilt of node 2 : |0-0| = 0 (no children)
#     Tilt of node 3 : |0-0| = 0 (no children)
#     Tile of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; 
#         right subtree is just right child, so sum is 3)
#     Sum of every tilt : 0 + 0 + 1 = 1
# Example 2:
#                 4                   6
#                / \                 / \
#               2   9     --->      2   7
#              / \   \             / \   \
#             3   5   7           0   0   0
#
#     Input: root = [4,2,9,3,5,null,7]
#     Output: 15
#     Explanation: 
#     Tilt of node 3 : |0-0| = 0 (no children)
#     Tilt of node 5 : |0-0| = 0 (no children)
#     Tilt of node 7 : |0-0| = 0 (no children)
#     Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; 
#         right subtree is just right child, so sum is 5)
#     Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is 
#         just right child, so sum is 7)
#     Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, 
#         and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
#     Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
# Example 3:
#                 21                      3
#                /  \                   /   \
#              7     14                6     0
#             / \    / \      --->    / \   / \
#            1   1  1   1            0   0 0   0 
#           / \                     / \
#          3   3                   0   0
#
#     Input: root = [21,7,14,1,1,2,2,3,3]
#     Output: 9
# Constraints:
#     The number of nodes in the tree is in the range [0, 104].
#     -1000 <= Node.val <= 1000
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        # recursive binary tree search summation 
        # binarySum = 0
        tiltSum = 0
        
        def findSum(r: TreeNode):
            nonlocal tiltSum
            if r == None:
                return 0
            
            left = findSum(r.left)
            right = findSum(r.right)
            tilt = abs(left - right)
            tiltSum += tilt

            return left + right + r.val

        # binarySum = findSum(root)
        findSum(root)
        return tiltSum

        # def findSum(r: TreeNode):
        #     binaryStack = []
        #     binarySum = 0
        #     binaryStack.append(r)

        #     while len(binaryStack) != 0:
        #         node = binaryStack.pop()
        #         left = 0
        #         right = 0
        #         if node.left:
        #             binaryStack.append(node.left)
        #             left = node.left.val
        #         if node.right:
        #             binaryStack.append(node.right)
        #             right = node.right.val
        #         print(node.val, left, right)
        #         binarySum += abs(left - right)
        #         print('binarySum=',binarySum)

        #     print(binarySum)
        #     return binarySum
        # return findSum(root)

s = Solution()
#                 1                1
#                / \      --->    / \
#               2   3            0   0
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
solution = 1
output = s.findTilt(t1)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# #                 4                   6
# #                / \                 / \
# #               2   9     --->      2   7
# #              / \   \             / \   \
# #             3   5   7           0   0   0
t2 = TreeNode(4)
t2.left = TreeNode(2)
t2.left.left = TreeNode(3)
t2.left.right = TreeNode(5)
t2.right = TreeNode(9)
t2.right.right = TreeNode(7)
solution = 15
output = s.findTilt(t2)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# #                 21                      3
# #                /  \                   /   \
# #              7     14                6     0
# #             / \    / \      --->    / \   / \
# #            1   1  1   1            0   0 0   0 
# #           / \                     / \
# #          3   3                   0   0
# t3 = TreeNode(21)
# t3.left = TreeNode(7)
# t3.left.left = TreeNode(1)
# t3.left.right = TreeNode(1)
# t3.left.left.left = TreeNode(3)
# t3.left.left.right = TreeNode(3)
# t3.right = TreeNode(14)
# t3.right.left = TreeNode(1)
# t3.right.right = TreeNode(1)
# solution = 9
# output = s.findTilt(t3)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))