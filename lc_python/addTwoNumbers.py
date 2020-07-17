# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # aList = l1
        # bList = l2

        # while (aList):
        #     print(f"{aList.val} -> ", end = '')
        #     aList = aList.next
        # print('NULL')
        # while (bList):
        #     print(f"{bList.val} -> ", end = '')
        #     bList = bList.next
        # print('NULL')

        aList = l1
        bList = l2
        remainder = 0
        sumList = []
        firstNode = True
    
        while (aList and bList):
            sum = aList.val + bList.val + remainder
            remainder = 0
            if (sum > 9):
                remainder = int(sum / 10)
                sum = sum - 10
            sumList.append(sum)
            print(f"{sum} -> ", end='')
            aList = aList.next
            bList = bList.next

        while (aList):
            sum = aList.val + remainder
            remainder = 0
            if (sum > 9):
                remainder = int(sum / 10)
                sum = sum - 10
            sumList.append(sum)
            print(f"{sum} -> ", end='')
            aList = aList.next
        while (bList):
            sum = bList.val + remainder
            remainder = 0
            if (sum > 9):
                remainder = int(sum / 10)
                sum = sum - 10
            sumList.append(sum)
            print(f"{sum} -> ", end='')
            bList = bList.next

        if (remainder > 0):
            sumList.append(remainder)
            print(f"{remainder} -> ", end='')
        print('NULL')

        for n in sumList:
            if (firstNode):
                headNode = cur = ListNode(val = n)
                firstNode = False
            else:
                cur.next = ListNode(val = n)
                cur = cur.next
        
        return headNode

            
            

a1 = ListNode(val = 2)
a2 = ListNode(val = 4)
a3 = ListNode(val = 3)
a1.next = a2
a2.next = a3

b1 = ListNode(val = 5)
b2 = ListNode(val = 6)
b3 = ListNode(val = 4)
# b4 = ListNode(val = 2)
b1.next = b2
b2.next = b3
# b3.next = b4

s = Solution()
ll = s.addTwoNumbers(a1, b1)

while (ll):
    print(f"{ll.val} -> ", end='')
    ll = ll.next
print("NULL")