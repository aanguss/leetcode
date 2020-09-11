# https://leetcode.com/problems/search-a-2d-matrix-ii/
# Search a 2D Matrix II
# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
# Example:
#     Consider the following matrix:
#     [
#         [1,   4,  7, 11, 15],
#         [2,   5,  8, 12, 19],
#         [3,   6,  9, 16, 22],
#         [10, 13, 14, 17, 24],
#         [18, 21, 23, 26, 30]
#     ]
# Given target = 5, return true.
# Given target = 20, return false.
from typing import List
class Solution:
    def searchMatrixBrute(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        valueFound = False
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == target:
                    valueFound = True
                    break
        
        return valueFound

    def searchMatrixRows(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        valueFound = False
        for row in matrix:
            if target in row:
                valueFound = True
                break
        
        return valueFound

s = Solution()
input = [   [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]]
target = 5
solution = True
# output = s.searchMatrixBrute(input, target)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output)) # use some ternary
output = s.searchMatrixRows(input, target)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output)) # use some ternary

target = 20
solution = False
# output = s.searchMatrixBrute(input, target)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output)) # use some ternary
output = s.searchMatrixRows(input, target)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output)) # use some ternary
