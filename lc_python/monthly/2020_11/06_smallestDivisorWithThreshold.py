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
        if nums == None or len(nums) == 0 or threshold == None or threshold == 0:
            return 0
        debug = False
        divisor = 1
        
        def getSum(div):
            s = 0
            for i in nums:
                v = ( int(i / div) + (i % div > 0) )
                s += v
            return s

        ##### QUICKER Binary from Solutions #####       
        l = 1
        r = max(nums)
        while l < r:
            mid = l + (r - l) // 2
            if getSum(mid) <= threshold:
                r = mid
            else:
                l = mid + 1
        divisor = l
        if debug: print(divisor)

        return divisor
        
        ##### BINARY 1 to THRESHOLD #####
        # possibleSolutions = []
        # def binarySearch (l, r, t): 
        #     # s = 0
        #     # when r and l cross we know we have full search
        #     if r >= l: 
        #         mid = l + (r - l) // 2
        #         s = getSum(mid)
        #         if debug: print(mid, s)

        #         # if sum <= threshold store and search even smaller div for larger sum
        #         if s <= t:
        #             possibleSolutions.append(mid)
        #             return binarySearch(l, mid - 1, t)
        #         # needed sum needs to be smaller to need to increase divisor 
        #         elif s > t:
        #             return binarySearch(mid + 1, r, t)
        #     else: # min is not possible
        #         return 1
        
        # result = binarySearch(1, max(nums), threshold)

        # if debug: print(result)

        # possibleSolutions.sort()
        # if debug: print(possibleSolutions)
        # divisor = possibleSolutions[0]

        # return divisor

        ##### LOW TO HIGH #####
        # priorSum = threshold
        # for i in range(1, sum-1):
        #     numSum = 0
        #     for j in nums:
        #         val = ( int(j / i) + (j % i > 0) )
        #         numSum += val
        #         if debug: print(i,j,val,sum)
        #     if debug: print(sum)
        #     if numSum == threshold:
        #         if debug: print('matches threshold')
        #         divisor = i
        #         break
        #     elif numSum < threshold and priorSum > threshold:
        #         if debug: print('using previous')
        #         divisor = i
        #         break
        #     priorSum = sum
        #
        #     return divisor
        
        ##### HIGH TO LOW #####
        # startRange = 0
        # if threshold > sum:
        #     startRange = sum
        # else:
        #     startRange = threshold
        # for i in range(startRange - 1, 0, -1):
        #     numSum = 0
        #     for j in nums:
        #         val = ( int(j / i) + (j % i > 0) )
        #         numSum += val
        #         if debug: print(i,j,val,sum)
        #     if debug: print(sum)
        #     if numSum <= threshold:
        #         if debug: print('matches threshold')
        #         divisor = i
        #         break
        #     # elif numSum > threshold and priorSum < threshold:
        #     #     if debug: print('using previous')
        #     #     divisor = priorSum
        #     #     break
        #     priorSum = sum
        #
        #     return divisor

s = Solution()
nums = [1,2,5,9]
threshold = 6
solution = 5
output = s.smallestDivisor(nums, threshold)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

nums = [2,3,5,7,11]
threshold = 11
solution = 3
output = s.smallestDivisor(nums, threshold)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

nums = [19]
threshold = 5
solution = 4
output = s.smallestDivisor(nums, threshold)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

nums = [1,2,3]
threshold = 1000000
solution = 1
output = s.smallestDivisor(nums, threshold)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

nums = [91,41,78,86,8]
threshold = 114
solution = 3
output = s.smallestDivisor(nums, threshold)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

nums = [19]
threshold = 5
solution = 4
output = s.smallestDivisor(nums, threshold)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))