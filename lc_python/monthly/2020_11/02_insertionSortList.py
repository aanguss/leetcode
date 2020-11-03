# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3517/
# https://leetcode.com/problems/insertion-sort-list/
#
# Sort a linked list using insertion sort.
#
# A graphical example of insertion sort. The partial sorted list (black) 
# initially contains only the first element in the list.  With each 
# iteration one element (red) is removed from the input data and inserted 
# in-place into the sorted list
#
# Algorithm of Insertion Sort:
#     Insertion sort iterates, consuming one input element each repetition, 
#         and growing a sorted output list.
#     At each iteration, insertion sort removes one element from the input data, 
#         finds the location it belongs within the sorted list, and inserts it there.
#     It repeats until no input elements remain.
# Example 1:
#     Input: 4->2->1->3
#     Output: 1->2->3->4
# Example 2:
#     Input: -1->5->3->4->0
#     Output: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # listDictionary = {}
        if head == None:
            return None
        debug = False
        sortedListHead = ListNode(head.val)
        currentNode = head.next
        while currentNode:
            if debug: print('currentNode =', currentNode.val)
            sortedNode = sortedListHead
            while sortedNode:
                if sortedNode == sortedListHead and currentNode.val < sortedNode.val:
                    newNode = ListNode(currentNode.val)
                    newNode.next = sortedNode
                    sortedListHead = newNode
                    break
                elif sortedNode.next != None and currentNode.val >= sortedNode.val and currentNode.val < sortedNode.next.val:
                    newNode = ListNode(currentNode.val)
                    newNode.next = sortedNode.next
                    sortedNode.next = newNode
                    break
                elif sortedNode.next == None and currentNode.val >= sortedNode.val:
                    sortedNode.next = ListNode(currentNode.val)
                    break
                elif sortedNode.next == None and currentNode.val < sortedNode.val:
                    newNode = ListNode(currentNode.val)
                    newNode.next = sortedNode.next
                    sortedNode.next = newNode
                    break
                sortedNode = sortedNode.next
            currentNode = currentNode.next
        return sortedListHead
        

s = Solution()
print('\nProblem1')
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
# solution = 5
output = s.insertionSortList(head)
i = 0
while output:
    print(i, output.val)
    output = output.next
    i += 1
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# -1->5->3->4->0
print('\nProblem2')
head = ListNode(-1)
head.next = ListNode(5)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(0)
# solution = 5
output = s.insertionSortList(head)
i = 0
while output:
    print(i, output.val)
    output = output.next
    i += 1
