# https://leetcode.com/explore/featured/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3523/
# https://leetcode.com/problems/two-sum-less-than-k/
#
# Given an array A of integers and integer K, return the maximum S such that 
# there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist 
# satisfying this equation, return -1.
#
# Example 1:
#     Input: A = [34,23,1,24,75,33,54,8], K = 60
#     Output: 58
#     Explanation: We can use 34 and 24 to sum 58 which is less than 60.
# Example 2:
#     Input: A = [10,20,30], K = 15
#     Output: -1
#     Explanation: In this case it is not possible to get a pair sum less that 15.
# Constraints:
#     1 <= A.length <= 100
#     1 <= A[i] <= 1000
#     1 <= K <= 2000
#
from typing import List
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if A == None or len(A) == 0:
            return -1
        if K == None or K <= 0:
            return -1

        A.sort()
        maxValue = -1
        l = 0
        r = len(A) - 1
        while l < r:
            val = A[l] + A[r]
            if val < K:
                if val > maxValue:
                    maxValue = val
                l += 1
            else:
                r -= 1
        return maxValue
        
        #### NESTED FOR is TOO SLOW ####
        # maxValue = -1
        # for i in range(len(A)):
        #     for j in range(i + 1, len(A)):
        #         val = A[i] + A[j]
        #         if val < K and val > maxValue:
        #             maxValue = val
        #             # print(maxValue, i, j, A[i], A[j])
        # return maxValue

s = Solution()
#     Input: A = [34,23,1,24,75,33,54,8], K = 60
#     Output: 58
A = [34,23,1,24,75,33,54,8]
K = 60
solution = 58
output = s.twoSumLessThanK(A, K)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

#     Input: A = [10,20,30], K = 15
#     Output: -1
A = [10,20,30]
K = 15
solution = -1
output = s.twoSumLessThanK(A, K)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

A = [358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549]
K = 1800
solution = 1794
output = s.twoSumLessThanK(A, K)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))