# https: // leetcode.com/discuss/interview-question/372434
# Given an int array nums and an int target, find how many unique pairs in 
# the array such that their sum is equal to target. Return the number of pairs.
#
# Example 1:
#     Input: nums = [1, 1, 2, 45, 46, 46], target = 47
#     Output: 2
#     Explanation:
#     1 + 46 = 47
#     2 + 45 = 47
# Example 2:
#     Input: nums = [1, 1], target = 2
#     Output: 1
#     Explanation:
#     1 + 1 = 2
# Example 3:
#     Input: nums = [1, 5, 1, 5], target = 6
#     Output: 1
#     Explanation:
#     [1, 5] and [5, 1] are considered the same.
# Related problems:
#     https: // leetcode.com/problems/two-sum
#     https: // leetcode.com/problems/two-sum-ii-input-array-is-sorted
from typing import List
class Solution:
    def findPairCount(self, nums, target):
        pairCount = 0
        pairList = []
        lenNum = len(nums)

        for i in range(lenNum):
            for j in range(i, lenNum):
                if (nums[i] + nums[j] == target):
                    if nums[i] < nums[j]:
                        if [nums[i], nums[j]] not in pairList:
                            pairList.append([nums[i], nums[j]])
                    else:
                        if [nums[j], nums[i]] not in pairList:
                            pairList.append([nums[j], nums[i]])
        print(pairList)
        pairCount = len(pairList)

        return pairCount

s = Solution()
nums = [1, 1, 2, 45, 46, 46]
target = 47
solution = 2
output = s.findPairCount(nums, target)
print("%s | %s" % ("PASS" if (output == solution) else "FAIL", output))

nums = [1, 1]
target = 2
solution = 1
output = s.findPairCount(nums, target)
print("%s | %s" % ("PASS" if (output == solution) else "FAIL", output))

nums = [1, 5, 1, 5]
target = 6
solution = 1
output = s.findPairCount(nums, target)
print("%s | %s" % ("PASS" if (output == solution) else "FAIL", output))
