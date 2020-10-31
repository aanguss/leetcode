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
        if root.val:
            print(root.val)
        if root.left: 
            self.printTree(root.left)
        if root.right:
            self.printTree(root.right)

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        debug = False
        allValues = []
        def getArray(n):
            if n.left:
                getArray(n.left)
            if n.val:
                allValues.append(n.val)
            if n.right:
                getArray(n.right)
        getArray(root)
        if debug: print(allValues)

        # find out of order indexes
        val1 = -1
        val2 = -1

        for i in range(len(allValues)):
            for j in range(i,len(allValues)):
                if allValues[j] - allValues[i] == -1:
                    if debug: print('allvalues[%d] - allValues[%d] == %d' % (j, i, allValues[j] - allValues[i]))
                    val1 = allValues[i]
                    val2 = allValues[j]
                    allValues[j] = val1
                    allValues[i] = val2
                    break
        if debug: print(val1, val2)

        def swapNodes(n):
            if n.val == val1:
                n.val = val2
            elif n.val == val2:
                n.val = val1
            if n.left:
                swapNodes(n.left)
            if n.right:
                swapNodes(n.right)
        swapNodes(root)

        allValues = []
        getArray(root)
        
        if debug: print(allValues)
        
        

s = Solution()
# root = [1,3,null,null,2]
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(2)
s.printTree(root)
s.recoverTree(root)
# inputPosition = 1
# solution = 1
# output = s.detectCycle(inputHead)
# print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

