# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3497/
# https://leetcode.com/problems/search-a-2d-matrix/
#
# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
#
# Example 1:
#     Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
#     Output: true
# Example 2:
#     Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
#     Output: false
# Example 3:
#     Input: matrix = [], target = 0
#     Output: false
# Constraints:
#     m == matrix.length
#     n == matrix[i].length
#     0 <= m, n <= 100
#     -10^4 <= matrix[i][j], target <= 10^4
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0 or target is None:
            return False

        rowLen = len(matrix)
        colLen = len(matrix[0])

        for i in range(rowLen):
            if target >= matrix[i][0] and target <= matrix[i][colLen-1]:
                # print('found %s in row %s' % (target, i))
                for j in range(colLen):
                    if target == matrix[i][j]:
                        return True
                break

        return False
        

s = Solution()
input_val1 = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
input_val2 = 3
solution = True
output = s.searchMatrix(input_val1, input_val2)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

input_val1 = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
input_val2 = 13
solution = False
output = s.searchMatrix(input_val1, input_val2)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

input_val1 = []
input_val2 = 0
solution = False
output = s.searchMatrix(input_val1, input_val2)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))