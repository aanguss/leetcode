# https://leetcode.com/problems/largest-number/
#
# Given a list of non negative integers, arrange them such that they form the largest number.
#
# Example 1:
#     Input: [10,2]
#     Output: "210"
# Example 2:
#     Input: [3,30,34,5,9]
#     Output: "9534330"
# Note: The result may be very large, so you need to return a string instead of an integer.
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        debug = True
        largestNum = ''
        if debug: print(nums)
        # bubble sort nums
        # nums.sort(key=lambda x: str(x)[0], reverse=True)
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        maxStringLen = len(max(nums, key=len))
        for currentDigit in range(maxStringLen):
            for i in range(len(nums)):
                for m in range(i + 1, len(nums)):
                    if debug: print("%s vs %s -- %s" % (nums[i], nums[m], nums))

                    if currentDigit < len(nums[i]) and currentDigit < len(nums[m]):
                        if debug: print("a - %s vs %s" % (nums[i][currentDigit], nums[m][currentDigit]))
                        if nums[i][currentDigit] < nums[m][currentDigit]:
                            if debug: print("a - swap")
                            temp = nums[m]
                            nums[m] = nums[i]
                            nums[i] = temp
                    elif currentDigit < len(nums[i]) and currentDigit >= len(nums[m]):
                        if debug: print("b - %s vs %s" % (nums[i][:currentDigit - 1], nums[m][:currentDigit - 1]))
                        if nums[i][:currentDigit - 1] == nums[m][:currentDigit - 1]:
                            if debug: print("b - swap")
                            temp = nums[i]
                            nums[i] = nums[m]
                            nums[m] = temp
                        break
                    elif currentDigit > len(nums[i]) and currentDigit < len(nums[m]):
                        if debug: print("c - %s vs %s" % (nums[i][:currentDigit - 1], nums[m][:currentDigit - 1]))
                        if nums[i][:currentDigit - 1] == nums[m][:currentDigit - 1]:
                            if debug: print("c - swap")
                            temp = nums[m]
                            nums[m] = nums[i]
                            nums[i] = temp
                        break
        
        if debug: print(nums)
        for num in nums:
            if debug: print(num)
            largestNum += str(num)
        return largestNum

s = Solution()
nums = [10,2]
solution = "210"
output = s.largestNumber(nums)
print("%s | %s" % ('PASS' if output == solution else 'FAIL', output))

nums = [3,30,34,5,9]
solution = "9534330"
output = s.largestNumber(nums)
print("%s | %s" % ('PASS' if output == solution else 'FAIL', output))

nums = [20,1]
solution = "201"
# output = s.largestNumber(nums)
# print("%s | %s" % ('PASS' if output == solution else 'FAIL', output))

nums = [121,12]
solution = "12121"
# output = s.largestNumber(nums)
# print("%s | %s" % ('PASS' if output == solution else 'FAIL', output))
