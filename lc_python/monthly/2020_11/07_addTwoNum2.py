# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3522/
# https://leetcode.com/problems/add-two-numbers-ii/
#
# You are given two non-empty linked lists representing two non-negative 
# integers. The most significant digit comes first and each of their nodes 
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
#     What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
# Example:
#     Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
#     Output: 7 -> 8 -> 0 -> 7
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        debug = False
        c1 = l1
        v1 = []
        c2 = l2
        v2 = []
        sum = []
        remainder = 0

        while c1 and c2:
            v1.append(c1.val)
            v2.append(c2.val)
            c1 = c1.next
            c2 = c2.next
        while c1:
            v1.append(c1.val)
            c1 = c1.next
        while c2:
            v2.append(c2.val)
            c2 = c2.next
        v1.reverse()
        v2.reverse()
        if debug: print(v1)
        if debug: print(v2)

        i = 0
        len1 = len(v1)
        len2 = len(v2)
        while True:
            if i < len1 and i < len2:
                sum.append(remainder + v1[i] + v2[i])
                if sum[i] >= 10:
                    remainder = sum[i] // 10
                    sum[i] = sum[i] % 10
                else:
                    remainder = 0
            elif i < len1:
                sum.append(remainder + v1[i])
                if sum[i] >= 10:
                    remainder = sum[i] // 10
                    sum[i] = sum[i] % 10
                else:
                    remainder = 0
            elif i < len2:
                sum.append(remainder + v2[i])
                if sum[i] >= 10:
                    remainder = sum[i] // 10
                    sum[i] = sum[i] % 10
                else:
                    remainder = 0
            elif remainder > 0:
                if debug: print(remainder)
                sum.append(remainder)
                break
            else:
                break
            i += 1
        sum.reverse()
        if debug: print(sum)

        
        headNode = None
        for i in sum:
            if headNode == None:
                currentNode = ListNode(i)
                headNode = currentNode
            else:
                currentNode.next = ListNode(i)
                currentNode = currentNode.next

        return headNode


s = Solution()
l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
solution = '7807'
current = s.addTwoNumbers(l1, l2)
output = ''
while current:
    output = output + str(current.val)
    current = current.next
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

l1 = ListNode(5)
l2 = ListNode(5)
solution = '10'
current = s.addTwoNumbers(l1, l2)
output = ''
while current:
    output = output + str(current.val)
    current = current.next
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))