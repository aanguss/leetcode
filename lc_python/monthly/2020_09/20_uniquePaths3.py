#!/usr/local/bin/python3.8

# https://leetcode.com/problems/unique-paths-iii/
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3466/
#
# Unique Paths III
# On a 2-dimensional grid, there are 4 types of squares:
#
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the 
# ending square, that walk over every non-obstacle square exactly once.
#
# Example 1:
# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
#
# Example 2:
# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
#
# Example 3:
# Input: [[0,1],[2,0]]
# Output: 0
# Explanation: 
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
#
# Note:
# 1 <= grid.length * grid[0].length <= 20
# class Solution:
from typing import List
def uniquePathsIII(grid: List[List[int]]) -> int:
    paths = 0

    rowSize = len(grid)
    colSize = len(grid[0])
    startRow = 0
    startCol = 0
    badNodes = 0

    # currentNode = grid[0]
    stack = []
    # visited = []

    # find starting position
    for row in range(rowSize):
        for col in range(colSize):
            if grid[row][col] == 1:
                startRow = row
                startCol = col
                # break
            if grid[row][col] == -1:
                badNodes += 1
    n_length = len(grid) * len(grid[0]) - badNodes

    stack.append([startRow,startCol])
    while stack:
        # currentNode = []
        # currentNode.append(stack.pop())
        currentNode = stack.pop()
        print(currentNode)

        print(currentNode[0])
        print(currentNode[1])

        

        # if currentNode not in visited:
        #     if grid[currentNode[0]][currentNode[1]] == 2:
        #         print("found result")
        #         paths += 1
        #         visited.append(currentNode)
        #     else:
        #         visited.append(currentNode)
        #         grid[currentNode[0]][currentNode[1]] = -1
        if grid[currentNode[0]][currentNode[1]] == 2 and :
            print("found result")
            paths += 1
            # visited.append(currentNode)

        print(currentNode[0])
        if currentNode[0] - 1 >= 0:
            if grid[currentNode[0] - 1][currentNode[1]] == 0 or grid[currentNode[0] - 1][currentNode[1]] == 2:
                stack.append([currentNode[0] - 1, currentNode[1]])
        if currentNode[0] + 1 < rowSize:
            if grid[currentNode[0] + 1][currentNode[1]] == 0 or grid[currentNode[0] + 1][currentNode[1]] == 2:
                stack.append([currentNode[0] + 1, currentNode[1]])
        if currentNode[1] - 1 >= 0:
            if grid[currentNode[0]][currentNode[1] - 1] == 0 or grid[currentNode[0]][currentNode[1] - 1] == 2:
                stack.append([currentNode[0], currentNode[1] - 1])
        if currentNode[1] + 1 < colSize:
            if grid[currentNode[0]][currentNode[1] + 1] == 0 or grid[currentNode[0]][currentNode[1] + 1] == 2:
                stack.append([currentNode[0], currentNode[1] + 1])

    

    return paths

input = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
solution = 2
output = uniquePathsIII(input)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))