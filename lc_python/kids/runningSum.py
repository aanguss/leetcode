# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        newList = []
        for i in nums:
            newList.append(total)
            total = total + i
            print(total)

    def printName(self):
        print("my name is tony")

s = Solution()
s.runningSum( [1,2,3,4] )
s.printName()

