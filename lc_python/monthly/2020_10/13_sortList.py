# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3493/
# https://leetcode.com/problems/sort-list/
#
# Given the head of a linked list, return the list after sorting it in 
# ascending order.
#
# Follow up: Can you sort the linked list in O(n logn) time and O(1) 
# memory (i.e. constant space)?
#
# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#
# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#
# Example 3:
# Input: head = []
# Output: []
#
# Constraints:
# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if head is None:
            return None
            
        sortedNodeDict = {}
        n = head
        while (n):
            sortedNodeDict[n] = n.val
            n = n.next

        sortedNodeDict = sorted(sortedNodeDict.items(), key=lambda x: x[1])
        
        firstNode = True

        for i in sortedNodeDict:
            if firstNode:
                headNode = i[0]
                node = headNode
                firstNode = False
            else:
                node.next = i[0]
                node = node.next
        node.next = None
                
        return headNode
            


s = Solution()
n = ListNode()
inputHead = [4,2,1,3]
nHead = n
for i in range(len(inputHead)):
    n.val = inputHead[i]
    if i != len(inputHead) - 1:
        n.next = ListNode()
        n = n.next
output = []
outputHead = s.sortList(nHead)
n = outputHead
for i in range(len(inputHead)):
    # print(n.val)
    output.append(n.val)
    n = n.next
solution = [1,2,3,4]
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))


n = ListNode()
inputHead = [-1,5,3,4,0]
nHead = n
for i in range(len(inputHead)):
    n.val = inputHead[i]
    if i != len(inputHead) - 1:
        n.next = ListNode()
        n = n.next
output = []
outputHead = s.sortList(nHead)
n = outputHead
for i in range(len(inputHead)):
    # print(n.val)
    output.append(n.val)
    n = n.next
solution = [-1,0,3,4,5]
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))



n = ListNode()
inputHead = []
nHead = n
for i in range(len(inputHead)):
    n.val = inputHead[i]
    if i != len(inputHead) - 1:
        n.next = ListNode()
        n = n.next
output = []
outputHead = s.sortList(nHead)
n = outputHead
for i in range(len(inputHead)):
    # print(n.val)
    output.append(n.val)
    n = n.next
solution = []
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

