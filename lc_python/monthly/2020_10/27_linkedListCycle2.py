# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3509/# https://leetcode.com/problems/champagne-tower/
# https://leetcode.com/problems/linked-list-cycle-ii/
#
# Given a linked list, return the node where the cycle begins. 
# If there is no cycle, return null.
#
# There is a cycle in a linked list if there is some node in 
# the list that can be reached again by continuously following 
# the next pointer. Internally, pos is used to denote the index 
# of the node that tail's next pointer is connected to. Note 
# that pos is not passed as a parameter.
#
# Notice that you should not modify the linked list.
#
# Follow up:
#     Can you solve it using O(1) (i.e. constant) memory?
#
# Example 1:
#     Input: head = [3,2,0,-4], pos = 1
#     Output: tail connects to node index 1
#     Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:
#     Input: head = [1,2], pos = 0
#     Output: tail connects to node index 0
#     Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Example 3:
#     Input: head = [1], pos = -1
#     Output: no cycle
#     Explanation: There is no cycle in the linked list.
# Constraints:
#     The number of the nodes in the list is in the range [0, 104].
#     -105 <= Node.val <= 105
#     pos is -1 or a valid index in the linked-list.

# from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        debug = False
        nodeDict = {}
        currentNode = head
        index = 0
        while currentNode:
            if debug: print('currentNode.val =', currentNode.val)
            if currentNode in nodeDict:
                # return nodeDict[currentNode]
                return currentNode
            else:
                nodeDict[currentNode] = index
            index += 1
            currentNode = currentNode.next
        return None

s = Solution()
inputHead = ListNode(3)
inputHead.next = ListNode(0)
inputHead.next.next = ListNode(-4)
inputHead.next.next.next = inputHead.next
inputPosition = 1
solution = 1
output = s.detectCycle(inputHead)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

