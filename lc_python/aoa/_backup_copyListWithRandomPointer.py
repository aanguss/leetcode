# https: // leetcode.com/problems/copy-list-with-random-pointer/
# A linked list is given such that each node contains an additional random 
# pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. 
# Each node is represented as a pair of[val, random_index] where:
#     val: an integer representing Node.val
#     random_index: the index of the node(range from 0 to n-1) where random pointer 
#         points to, or null if it does not point to any node.
#
# Example 1:
#     Input: head = [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
#     Output: [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
#
# Example 2:
#     Input: head = [[1, 1], [2, 1]]
#     Output: [[1, 1], [2, 1]]
#
# Example 3:
#     Input: head = [[3, null], [3, 0], [3, null]]
#     Output: [[3, null], [3, 0], [3, null]]
#
# Example 4:
#     Input: head = []
#     Output: []
#     Explanation: Given linked list is empty(null pointer), so return null.
#
# Constraints:
#     -10000 <= Node.val <= 10000
#     Node.random is null or pointing to a node in the linked list.
#     Number of Nodes will not exceed 1000.
from typing import List

# Definition for a Node.
class Node:
    # def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def createNodeFromList(self, nums):
        if not nums or len(nums) == 0:
            return None
        head = True
        for item in nums:
            # print(item)
            if head:
                n = Node(item[0])
                n_head = n
                head = False
            else:
                n.next = Node(item[0])
                n = n.next
            n.random = item[1]

        return n_head

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None

        linkListDict = {}
        linkListValDict = {}
        valDict = {}
        index = 0
        
        headNode = True
        headCopy = head
        while headCopy:
            if headNode:
                n = Node(headCopy.val)
                n_head = n
                headNode = False
            else:
                n.next = Node(headCopy.val)
                n = n.next
            
            if headCopy.random == None:
                n.random = None
                linkListValDict.update({index: None})
            else:
                tempNode = headCopy.random
                # n.random = headCopy.random
                linkListValDict.update({index: tempNode.val})
            valDict.update({n.val: n})
            linkListDict.update({index:n})
            index += 1

            headCopy = headCopy.next
        
        # now to get all the random pointer objects
        n = n_head
        index = 0
        while n:
            n.random = linkListDict[index]
            index += 1
            n = n.next
            # if not headCopy.random and headCopy.random != 0:
            #     n.random = None
            # else:
            #     n.random = headCopy.random

            # headCopy = headCopy.next
        
        return n_head

# s = Solution()
# head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
# solution = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
# # output = s.copyRandomList(head)
# # print("%s | output = %s" % (output == solution, output))

# head = [[1, 1], [2, 1]]
# solution = [[1, 1], [2, 1]]

# head = [[3, None], [3, 0], [3, None]]
# solution = [[3, None], [3, 0], [3, None]]

# head = []
# solution = []

s = Solution()
input = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
head = s.createNodeFromList(input)
n = head
output = []
while(n):
    output.append([n.val, n.random])
    n = n.next
print(output)
new_head = s.copyRandomList(head)
n = new_head
output = []
while(n):
    output.append([n.val, n.random])
    n = n.next
print(output)
