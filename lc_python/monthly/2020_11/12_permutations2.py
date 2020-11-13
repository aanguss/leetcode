# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3528/
# https://leetcode.com/problems/permutations-ii/
#
# Given a collection of numbers, nums, that might contain duplicates, return all 
# possible unique permutations in any order. 
#
# Example 1:
#     Input: nums = [1,1,2]
#     Output:
#     [[1,1,2],
#     [1,2,1],
#     [2,1,1]]
# Example 2:
#     Input: nums = [1,2,3]
#     Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Constraints:
#     1 <= nums.length <= 8
#     -10 <= nums[i] <= 10
#
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums == None or len(nums) == 0:
            return [[]]
        newList = []

        for i in range(len(nums)):
            subList = []
            for j in range(len(nums)):
                j += i
                if j >= len(nums):
                    j -= len(nums)
                subList.append(nums[j])
            newList.append(subList)
        # print(newList)
        return newList

s = Solution()
nums = [1,1,2]
solution = [[1,1,2],[1,2,1],[2,1,1]]
output = s.permuteUnique(nums)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

nums = [1,2,3]
solution = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
output = s.permuteUnique(nums)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))