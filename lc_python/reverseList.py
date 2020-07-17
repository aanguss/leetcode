# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head is None):
            return head
        elif(head.next is None):
            return head

        linkedList = head
        # revLinkedList
        firstNode = True
        newHead = ListNode()
        while (linkedList.next):
            # print(f"{linkedList.val} points to {linkedList.next.val}")
            nextNode = linkedList.next
            # print(f"\t nextNode = {nextNode.val}")
            # if(curNode is not None):
            if(firstNode):
                firstNode = False
                linkedList.next = None
            else:
                # print(f"\t preCurNode - linkedList.next = {linkedList.next.val}")
                linkedList.next = curNode
                # print(f"\t postCurNode - linkedList.next = {linkedList.next.val}")
            curNode = linkedList
            # print(f"\t curNode now - {curNode.val}")
            # print(f"\t nextNode.val = {nextNode.val}")
            if (nextNode is None):
                # printf("nextNode is None")
                newHead = curNode
            linkedList = nextNode
        linkedList.next = curNode
        newHead = linkedList
        return newHead 
        

# l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
# l5.next = None

# a) save dummy next
# b) if (prev) then set to new next
# c) save prev to current
# d) go to dummy next



s = Solution()
l1 = ListNode(val = 1)
l2 = ListNode(val = 2)
l3 = ListNode(val = 3)
l4 = ListNode(val = 4)
l5 = ListNode(val = 5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

l = l1
while(l):
    print(f"{l.val} -> ", end='')
    l = l.next
print("NULL")

newLL = s.reverseList(l1)
while(newLL):
    print(f"{newLL.val} -> ", end='')
    newLL = newLL.next
print("NULL")