# https://leetcode.com/explore/featured/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3516/
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
#
# Given head which is a reference node to a singly-linked list. The value of 
# each node in the linked list is either 0 or 1. The linked list holds the 
# binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# Example 1:
#     Input: head = [1,0,1]
#     Output: 5
#     Explanation: (101) in base 2 = (5) in base 10
# Example 2:
#     Input: head = [0]
#     Output: 0
# Example 3:
#     Input: head = [1]
#     Output: 1
# Example 4:
#     Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
#     Output: 18880
# Example 5:
#     Input: head = [0,0]
#     Output: 0
# Constraints:
#     The Linked List is not empty.
#     Number of nodes will not exceed 30.
#     Each node's value is either 0 or 1.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        i = 0
        node = head
        nodeValues = []
        while node:
            nodeValues.append(node.val)
            node = node.next
        nodeValues.reverse()
        for i in range(len(nodeValues)):
            # print("2^i =", 2**i)
            decimal += (nodeValues[i] * 2**i)
        return decimal

s = Solution()
# head = [1,0,1]
head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
solution = 5
output = s.getDecimalValue(head)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))


# [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# head = ListNode(1)
# head.next
# solution = 18880