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
    def __init(self):
        pass

    def createNodeFromList(self, nums):
        if not nums or len(nums) == 0:
            return None
        visitedNode = {}
        head = True
        for item in nums:
            # print(item)
            if head:
                n = Node(item[0])
                visitedNode[n] = n
                n_head = n
                head = False
            else:
                n.next = Node(item[0])
                if n.next != None:
                    if n.next in visitedNode:
                        n.next = visitedNode[n.next]
                    else:
                        visitedNode[n.next] = Node(n.next.val)
                        n.next = visitedNode[n.next]
                n = n.next
            n.random = item[1]
            if n.random != None:
                if n.random in visitedNode:
                    n.random = visitedNode[n.random]
                else:
                    visitedNode[n.random] = Node(n.random)
                    n.random = visitedNode[n.random]


        return n_head

    # modified version of https://leetcode.com/problems/copy-list-with-random-pointer/solution/
    def copyRandomList(self, head):
        if not head:
            return None
        visitedNode = {}

        n = head
        # Creating the new head node.
        newHead = Node(n.val)
        visitedNode[n] = newHead

        # Iterate on the linked list until all nodes are cloned.
        while n:
            # handle random with new node if not already seen
            if n.random == None:
                newHead.random = None
            elif n.random in visitedNode:
                newHead.random = visitedNode[n.random]
            else:
                visitedNode[n.random] = Node(n.random.val)
                newHead.random = visitedNode[n.random]
            
            # handle next with new node if not already seen
            if n.next == None:
                newHead.next = None
            elif n.next in visitedNode:
                newHead.next = visitedNode[n.next]
            else:
                visitedNode[n.next] = Node(n.next.val)
                newHead.next = visitedNode[n.next]

            # Move one step ahead in the linked list.
            n = n.next
            newHead = newHead.next

        return visitedNode[head]

s = Solution()
input = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
head = s.createNodeFromList(input)
n = head
output = []
while(n):
    if n.random == None:
        output.append([n.val, n.random])
    else:
        tempHead = n.random
        output.append([n.val, tempHead.val])
    n = n.next
print(output)
new_head = s.copyRandomList(head)
n = new_head
output = []
while(n):
    if n.random == None:
        output.append([n.val, n.random])
    else:
        tempHead = n.random
        output.append([n.val, tempHead.val])
    n = n.next
print(output)
