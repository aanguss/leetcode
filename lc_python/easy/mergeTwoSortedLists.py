# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:
#   Input: 1->2->4, 1->3->4
#   Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def printLinkedList(self, ll):
        while(ll):
            print("%d" % ll.val, end = '->')
            ll = ll.next
        print('\n')

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        firstNode = True
        l3_head = None
        while (l1 and l2):
            # print("both true")
            if firstNode:
                l3 = ListNode()
                l3_head = l3
                firstNode = False
            else:
                l3.next = ListNode()
                l3 = l3.next
            
            if (l1.val < l2.val):
                l3.val = l1.val
                # print("l1.val > l2.val (%d > %d) = %d, l3 = %d" % (l1.val, l2.val, (l1.val > l2.val), l3.val))
                l1 = l1.next
            else:
                l3.val = l2.val
                # print("l1.val < l2.val (%d > %d) = %d, l3 = %d" % (l1.val, l2.val, (l1.val <= l2.val), l3.val))
                l2 = l2.next
        while (l1):
            if firstNode:
                l3 = ListNode()
                l3_head = l3
                firstNode = False
            else:
                l3.next = ListNode()
                l3 = l3.next
            l3.val = l1.val
            # print("l1 (%d) = %d" % (l1.val, l3.val))
            l1 = l1.next
        while (l2):
            if firstNode:
                l3 = ListNode()
                l3_head = l3
                firstNode = False
            else:
                l3.next = ListNode()
                l3 = l3.next
            l3.val = l2.val
            # print("l2 (%d) = %d" % (l2.val, l3.val))
            l2 = l2.next
        # print("\n")
        return l3_head

list1 = ListNode()
list1.val = 3
list1.next = ListNode()
list1.next.val = 4
list1.next.next = ListNode()
list1.next.next.val = 5
list2 = ListNode()
list2.val = 1
list2.next = ListNode()
list2.next.val = 2
list2.next.next = ListNode()
list2.next.next.val = 3
s = Solution()


s.printLinkedList(list1)
s.printLinkedList(list2)
list3 = s.mergeTwoLists(list1,list2)
s.printLinkedList(list3)