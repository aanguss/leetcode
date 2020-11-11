# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3526/# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# https://leetcode.com/problems/flipping-an-image/
#
# Given a binary matrix A, we want to flip the image horizontally, then invert 
#   it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.  
#   For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
#
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced 
#   by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
#
# Example 1:
#        1 1 0           1 0 0
#        1 0 1   -->     0 1 0
#        0 0 0           1 1 1
#     Input: [[1,1,0],[1,0,1],[0,0,0]]
#     Output: [[1,0,0],[0,1,0],[1,1,1]]
#     Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
#     Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:
#        1 1 0 0           1 1 0 0
#        1 0 0 1   -->     0 1 1 0
#        0 1 1 1           0 0 0 1
#        1 0 1 0           1 0 1 0
#     Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
#     Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#     Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
#     Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Notes:
#     1 <= A.length = A[0].length <= 20
#     0 <= A[i][j] <= 1
#
from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if A == None or len(A) == 0 or len(A[0]) == 0:
            return [[]]
        # reverse
        for a in A:
            l = 0
            r = len(a) - 1
            while l < r:
                temp = a[l]
                a[l] = a[r]
                a[r] = temp
                l += 1
                r -= 1
        # invert
        for a in A:
            for i in range(len(a)):
                if a[i] == 0:
                    a[i] = 1
                else:
                    a[i] = 0
        return A

s = Solution()
inputList = [[1,1,0],[1,0,1],[0,0,0]]
solution = [[1,0,0],[0,1,0],[1,1,1]]
output = s.flipAndInvertImage(inputList)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

inputList = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
solution = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
output = s.flipAndInvertImage(inputList)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))
