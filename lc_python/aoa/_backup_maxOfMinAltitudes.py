# https: // leetcode.com/discuss/interview-question/383669/
# Given a matrix with r rows and c columns, find the maximum score of a path 
# starting at[0, 0] and ending at[r-1, c-1]. The score of a path is the minimum 
# value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.
#
# Don't include the first or final entry. You can only move either down or right 
# at any point in time.
#
# Example 1:
#     Input:
#         [[5, 1],
#         [4, 5]]
#     Output: 
#         4
#     Explanation:
#         Possible paths:
#             5 → 1 → 5 = > min value is 1
#             5 → 4 → 5 = > min value is 4
#         Return the max value among minimum values = > max(4, 1) = 4.
# Example 2:
#     Input:
#         [[1, 2, 3]
#         [4, 5, 1]]
#     Output: 
#         4
#     Explanation:
#         Possible paths:
#             1 -> 2 -> 3 -> 1
#             1 -> 2 -> 5 -> 1
#             1 -> 4 -> 5 -> 1
#         So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
#         Return the max of that, so 4.
# Related problems:
#     https: // leetcode.com/problems/minimum-path-sum/
#     https: // leetcode.com/problems/unique-paths-ii/
#     https: // leetcode.com/problems/path-with-maximum-minimum-value(premium) is a different problem. In this problem we can only move in 2 directions.
from typing import List
class Solution:
    def findMaxOfMins(self, matrix):
        minValue = None
        
        # FAIL #1
        # pathList = []
        # rowLen = len(matrix)
        # colLen = len(matrix[0])
        # # starting location
        # row = 0
        # col = 0
        # stackList = []
        # currentNode = [row, col]
        # stackList.append(currentNode)
        # while True:
        #         # print("stackList = %s" % stackList)
                
        #     if currentNode:
        #         row = currentNode[0]
        #         col = currentNode[1]
        #         pathList.append(matrix[row][col])
        #         print(pathList)

        #         stackList.append([row, col])
        #         print("stacklist =",stackList)
                
        #         if row < rowLen:
        #             currentNode[0] += 1
        #     elif stackList:
        #         currentNode = stackList.pop()
        #         if col < colLen:
        #             currentNode[1] += 1
        #     else:
        #         break
        
        print(matrix)
        rowLen = len(matrix)
        colLen = len(matrix[0])
        print("rowlen =", rowLen)
        print("collen =", colLen)
        # find min from starting location: 0, 0
        minValue = self.getMin(matrix, 0, 0)

        return minValue
    
    def getMin(self, matrix, row, col):
        rowLen = len(matrix)
        colLen = len(matrix[0])

        print("testing [%d][%d]" % (row, col))
        
        if (row == rowLen or col == colLen):
            return 9999
        if (row == rowLen - 1 and col == colLen - 1):
            return matrix[row][col]
        # size = matrix[row][col] + min(self.getMin(matrix, row + 1, col), self.getMin(matrix, row, col + 1))
        size = min(matrix[row][col], self.getMin(matrix, row + 1, col), self.getMin(matrix, row, col + 1))
        return size

s = Solution()
input = [[5,1], [4,5]]
solution = 4
output = s.findMaxOfMins(input)
print("%s | %s" % ("PASS" if (output == solution) else "FAIL", output))

input = [[1, 2, 3], [4, 5, 1]]
solution = 4
output = s.findMaxOfMins(input)
print("%s | %s" % ("PASS" if (output == solution) else "FAIL", output))
