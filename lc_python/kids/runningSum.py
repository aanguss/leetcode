# https://leetcode.com/problems/running-sum-of-1d-array/
# i did this with the family
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        newList = []
        for i in nums:
            total = total + i
            newList.append(total)
            print(total)
        return newList

    def printName(self):
        print("my name is tony")

s = Solution()
totalList = []
totalList = s.runningSum( [1,2,3,4] )
s.printName()

for i in totalList:
    print(i)
