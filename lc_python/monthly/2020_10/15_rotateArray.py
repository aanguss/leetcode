# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3496/
# https://leetcode.com/problems/rotate-array/
#
# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Follow up:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
# Example 1:
#     Input: nums = [1,2,3,4,5,6,7], k = 3
#     Output: [5,6,7,1,2,3,4]
#     Explanation:
#     rotate 1 steps to the right: [7,1,2,3,4,5,6]
#     rotate 2 steps to the right: [6,7,1,2,3,4,5]
#     rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#     Input: nums = [-1,-100,3,99], k = 2
#     Output: [3,99,-1,-100]
#     Explanation: 
#     rotate 1 steps to the right: [99,-1,-100,3]
#     rotate 2 steps to the right: [3,99,-1,-100]
# Constraints:
#     1 <= nums.length <= 2 * 104
#     -231 <= nums[i] <= 231 - 1
#     0 <= k <= 105
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numLen = len(nums)
        tempArray = nums.copy()
        for i in range(len(nums)):
            newLoc = (i + k) % numLen
            nums[newLoc] = tempArray[i]

s = Solution()
input_nums = [1,2,3,4,5,6,7]
input_k = 3
solution_output = [5,6,7,1,2,3,4]
s.rotate(input_nums, input_k)
print("%s | %s" % ('PASS' if (input_nums == solution_output) else 'FAIL', input_nums))

input_nums = [-1,-100,3,99]
input_k = 2
solution_output = [3,99,-1,-100]
s.rotate(input_nums, input_k)
print("%s | %s" % ('PASS' if (input_nums == solution_output) else 'FAIL', input_nums))