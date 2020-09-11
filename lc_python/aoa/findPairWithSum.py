# https://leetcode.com/discuss/interview-question/356960
# Given a list of positive integers nums and an int target, return indices of 
# the two numbers such that they add up to a target - 30.
#
# Conditions:
#   You will pick exactly 2 numbers.
#   You cannot pick the same element twice.
#   If you have muliple pairs, select the pair with the largest number.
#
# Example 1:
#   Input: nums = [1, 10, 25, 35, 60], target = 90
#   Output: [2, 3]
#   Explanation:
#       nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
#
# Example 2:
#   Input: nums = [20, 50, 40, 25, 30, 10], target = 90
#   Output: [1, 5]
#   Explanation:
#       nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
#       nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
#
# You should return the pair with the largest number.
from typing import List
class Solution:
    def findPairWithSum(self, nums: List[int], target: int) -> List[int]:
        largestSumPair = []
        target = target - 30
        # print("target =", target)
        pairList = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if [i, j] not in pairList and [j, i] not in pairList:
                        pairList.append([i, j])

        # print(pairList)
        largestValue = pairList[0][0]
        largestPairIndex = 0
        for i in range(len(pairList)):
            if pairList[i][0] > largestValue:
                largestValue = pairList[i][0]
                largestPairIndex = i
            if pairList[i][1] > largestValue:
                largestValue = pairList[i][1]
                largestPairIndex = i
        

        return pairList[largestPairIndex]

s = Solution()
nums = [1, 10, 25, 35, 60]
target = 90
solution = [2, 3]
output = s.findPairWithSum(nums, target)
print("%s | %s" % (output == solution, output))


nums = [20, 50, 40, 25, 30, 10]
target = 90
solution = [1, 5]
output = s.findPairWithSum(nums, target)
print("%s | %s" % (output == solution, output))
