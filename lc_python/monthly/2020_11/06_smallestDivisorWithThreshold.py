# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3521/
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
#
# Given an array of integers nums and an integer threshold, we will choose 
# a positive integer divisor and divide all the array by it and sum the 
# result of the division. Find the smallest divisor such that the result 
# mentioned above is less than or equal to threshold.
#
# Each result of division is rounded to the nearest integer greater than 
# or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
#
# It is guaranteed that there will be an answer.
#
# Example 1:
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
#     If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the 
#     divisor is 5 the sum will be 5 (1+1+1+2). 
# Example 2:
#     Input: nums = [2,3,5,7,11], threshold = 11
#     Output: 3
# Example 3:
#     Input: nums = [19], threshold = 5
#     Output: 4
# Constraints:
#     1 <= nums.length <= 5 * 10^4
#     1 <= nums[i] <= 10^6
#     nums.length <= threshold <= 10^6
#
from typing import List
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        return 0

s = Solution()
nums = [1,2,5,9]
threshold = 6
solution = 5
output = s.smallestDivisor(nums, threshold)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# nums = [2,3,5,7,11]
# threshold = 11
# solution = 3
# output = s.smallestDivisor(nums, threshold)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# nums = [19]
# threshold = 5
# solution = 4
# output = s.smallestDivisor(nums, threshold)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))
