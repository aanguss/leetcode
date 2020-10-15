# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3494/
# https://leetcode.com/problems/house-robber-ii/
#
# You are a professional robber planning to rob houses along a street. Each 
# house has a certain amount of money stashed. All houses at this place are 
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have a security system connected, and it will
# automatically contact the police if two adjacent houses were broken into on 
# the same night.
#
# Given a list of non-negative integers nums representing the amount of money 
# of each house, return the maximum amount of money you can rob tonight without 
# alerting the police.
#
# Example 1:
#     Input: nums = [2,3,2]
#     Output: 3
#     Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:
#     Input: nums = [1,2,3,1]
#     Output: 4
#     Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#     Total amount you can rob = 1 + 3 = 4.
# Example 3:
#     Input: nums = [0]
#     Output: 0 
# Constraints:
#     1 <= nums.length <= 100
#     0 <= nums[i] <= 1000
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        ###############################
        # doesn't work for test case #5
        ###############################
        # debug = False
        # if nums is None:
        #     return 0

        # numHouses = len(nums)
        # if debug: print('numHouses =', numHouses)
        # if debug: print('numHouses % 2 =', numHouses % 2)
        # totalOddCash = 0
        # totalEvenCash = 0

        # if numHouses == 0:
        #     return 0

        # if numHouses == 1:
        #     return nums[0]

        # if numHouses == 2:
        #     if nums[0] > nums[1]:
        #         return nums[0]
        #     else:
        #         return nums[1]

        # if numHouses == 3:
        #     return nums[1]

        # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         if debug: print('adding', nums[i])
        #         totalEvenCash += nums[i]
        #         if debug: print('totalEven =', totalEvenCash)
        #     else:
        #         if debug: print('adding', nums[i])
        #         totalOddCash += nums[i]
        #         if debug: print('totalOdd =', totalOddCash)
        
        # if numHouses % 2 == 1:
        #     if debug: print('found == 1')
        #     if nums[0] > nums[numHouses-1]:
        #         if debug: print('nums[0] >')
        #         totalEvenCash -= nums[numHouses - 1]
        #         if debug: print('totalOdd =', totalOddCash)
        #     else:
        #         if debug: print('nums[numHouses-1] >')
        #         totalEvenCash -= nums[0]
        #         if debug: print('totalOdd =', totalOddCash)

        # if totalEvenCash > totalOddCash:
        #     return totalEvenCash
        # else:
        #     return totalOddCash
            


s = Solution()
inputVal = [2,3,2]
outputVal = s.rob(inputVal)
solution = 3
print("%s | %s" % ('PASS' if (outputVal == solution) else 'FAIL', outputVal))

inputVal = [1,2,3,1]
outputVal = s.rob(inputVal)
solution = 4
print("%s | %s" % ('PASS' if (outputVal == solution) else 'FAIL', outputVal))

inputVal = [0]
outputVal = s.rob(inputVal)
solution = 0
print("%s | %s" % ('PASS' if (outputVal == solution) else 'FAIL', outputVal))

inputVal = [200,3,140,20,10]
outputVal = s.rob(inputVal)
solution = 340
print("%s | %s" % ('PASS' if (outputVal == solution) else 'FAIL', outputVal))

inputVal = [1,3,1,3,100]
outputVal = s.rob(inputVal)
solution = 103
print("%s | %s" % ('PASS' if (outputVal == solution) else 'FAIL', outputVal))
