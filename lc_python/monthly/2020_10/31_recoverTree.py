# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/563/week-5-october-29th-october-31st/3514/
# https://leetcode.com/problems/recover-binary-search-tree/
#
# You are given the root of a binary search tree (BST), where exactly two nodes of 
# the tree were swapped by mistake. Recover the tree without changing its structure.
#
# Follow up: A solution using O(n) space is pretty straight forward. Could you 
# devise a constant space solution?
#
# Example 1:
#     Input: root = [1,3,null,null,2]
#     Output: [3,1,null,null,2]
#     Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
# Example 2:
#     Input: root = [3,1,4,null,null,2]
#     Output: [2,1,4,null,null,3]
#     Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
# Constraints:
#     The number of nodes in the tree is in the range [2, 1000].
#     -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def printTree(self, root):
        if root.val != None:
            print(root.val)
        if root.left != None: 
            self.printTree(root.left)
        if root.right != None:
            self.printTree(root.right)

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        debug = True
        allValues = []
        def getArray(n):
            if n.left != None:
                getArray(n.left)
            if n.val != None:
                allValues.append(n.val)
            if n.right != None:
                getArray(n.right)
        getArray(root)
        if debug: print(allValues)

        # find out of order indexes
        val1 = None
        val2 = None

        def findNums(allVal):
            v1 = None
            v2 = None
            for i in range(len(allVal) - 1):
                j = i + 1
                if debug: print('allVal[%d] = %d, allVal[%d] = %d' % (i, allVal[i], j, allVal[j]))
                if allVal[j] < allVal[i]:
                    v2 = allVal[j]
                    if v1 == None:
                        v1 = allVal[i]
            return v1,v2
        val1, val2 = findNums(allValues)

        if debug: print(val1, val2)

        def swapNodes(n):
            if n.left != None:
                swapNodes(n.left)
            if n.val == val1:
                n.val = val2
            elif n.val == val2:
                n.val = val1
            if n.right != None:
                swapNodes(n.right)
        swapNodes(root)

        allValues = []
        getArray(root)
        
        if debug: print(allValues)
        
        

s = Solution()
print('root1')
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.right = TreeNode(2)
s.printTree(root1)
s.recoverTree(root1)

print('root2')
root2 = TreeNode(3)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(2)
s.printTree(root2)
s.recoverTree(root2)

print('root3')
root3 = TreeNode(0)
root3.left = TreeNode(1)
s.printTree(root3)
s.recoverTree(root3)