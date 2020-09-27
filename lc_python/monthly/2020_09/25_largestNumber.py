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
class LargerNum(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        debug = True
        largestNum = ''
        if debug: print(nums)
        
        # def largerThan(x,y):
        #     return x+y > y+x
        
        largestNum = ''.join(sorted(map(str,nums),key=LargerNum))

        
        
        if debug: print(nums)
        # for num in nums:
        #     if debug: print(num)
        #     largestNum += str(num)
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
