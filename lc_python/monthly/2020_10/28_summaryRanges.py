# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3510/
# https://leetcode.com/problems/summary-ranges/
#
# You are given a sorted unique integer array nums.
#
# Return the smallest sorted list of ranges that cover all the 
# umbers in the array exactly. That is, each element of nums 
# is covered by exactly one of the ranges, and there is no 
# integer x such that x is in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
#    "a->b" if a != b
#    "a" if a == b
#
# Example 1:
#     Input: nums = [0,1,2,4,5,7]
#     Output: ["0->2","4->5","7"]
#     Explanation: The ranges are:
#     [0,2] --> "0->2"
#     [4,5] --> "4->5"
#     [7,7] --> "7"
# Example 2:
#     Input: nums = [0,2,3,4,6,8,9]
#     Output: ["0","2->4","6","8->9"]
#     Explanation: The ranges are:
#     [0,0] --> "0"
#     [2,4] --> "2->4"
#     [6,6] --> "6"
#     [8,9] --> "8->9"
# Example 3:
#     Input: nums = []
#     Output: []
# Example 4:
#     Input: nums = [-1]
#     Output: ["-1"]
# Example 5:
#     Input: nums = [0]
#     Output: ["0"]
# Constraints:
#     0 <= nums.length <= 20
#     -231 <= nums[i] <= 231 - 1
#     All the values of nums are unique.

from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums is None or len(nums) == 0:
            return []
        debug = False
        numList = []
        # startVal = ""
        # endVal = ""
        i = 0
        # for i in range(len(nums)):
        while i < len(nums):
            # startVal = "{0}".format(nums[i])
            # for j in range(i,len(nums)):
            if i + 1 < len(nums):
                j = i + 1
                while j < len(nums):
                    if nums[j]-nums[i] > 1:
                        numList.append("%d->%d" % (nums[i], nums[j-1]))
                    elif nums[j] - nums[i] == 1:
                        i += 1
                        j += 1
                    else:
                        j += 1

            if debug: print("found nums[i] =", nums[i])
            endVal = "{0}".format(nums[i])
            
        # if startVal is not "" and endVal is "":
        #     numList.append(startVal)
        return numList


s = Solution()
# input_nums = [0,1,2,4,5,7]
input_nums = [7]
solution = ["0->2","4->5","7"]
output = s.summaryRanges(input_nums)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

