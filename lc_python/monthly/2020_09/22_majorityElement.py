# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3469/
# https://leetcode.com/problems/majority-element-ii/
#
# Given an integer array of size n, find all elements that appear more 
# than ⌊ n/3 ⌋ times.
#
# Note: The algorithm should run in linear time and in O(1) space.
#
# Example 1:
# Input: [3,2,3]
# Output: [3]
#
# Example 2:
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        debug = False
        numsDict = {}
        returnNums = []
        minCount = len(nums) / 3
        if debug: print("mincount = %s" % (minCount))
        
        for i in range(len(nums)):
            if nums[i] in numsDict:
                numsDict[nums[i]] += 1
            else:
                numsDict[nums[i]] = 1
        if debug: print(numsDict)
        for key in numsDict:
            if numsDict[key] > minCount:
                returnNums.append(key)
        
        return returnNums