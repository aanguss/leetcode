# https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/894/
##
# Given a 2d grid map of '1's (land) and '0's (water), 
# count the number of islands. An island is surrounded by water 
# and is formed by connecting adjacent lands horizontally or 
# vertically. You may assume all four edges of the grid are all 
# surrounded by water.
##
# Example 1
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
##
# Example 2
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
from typing import List

class Solution:
        def __dfs(self, grid: List[List[str]], row: int, col: int):
            grid[row][col] = '0'
            if (row - 1 >= 0):
                if (grid[row - 1][col] == '1'):
                    self.__dfs(grid, row - 1, col)
            if (row + 1 < len(grid)):
                if (grid[row + 1][col] == '1'):
                    self.__dfs(grid, row + 1, col)
            if (col - 1 >= 0):
                if (grid[row][col - 1] == '1'):
                    self.__dfs(grid, row, col - 1)
            if (col + 1 < len(grid[0])):
                if (grid[row][col + 1] == '1'):
                    self.__dfs(grid, row, col + 1)

        def numIslands(self, grid: List[List[str]]) -> int:
            if not grid:
                return 0 # no islands since grid is empty
            islandCount = 0

            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if (grid[row][col] == '1'):
                        islandCount += 1
                        self.__dfs(grid, row, col)
            return islandCount
            
        

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
] # should return 1

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
] # should return 3

grid3 = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]] # should return 1

s = Solution()

islands = s.numIslands(grid1)
print(f"Number of islands on grid1 = {islands}")

islands = s.numIslands(grid2)
print(f"Number of islands on grid2 = {islands}")

islands = s.numIslands(grid3)
print(f"Number of islands on grid3 = {islands}")