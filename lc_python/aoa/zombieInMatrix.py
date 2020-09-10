# https://leetcode.com/discuss/interview-question/411357/
# Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can 
# turn adjacent(up/down/left/right) human beings into zombies every hour. 
# Find out how many hours does it take to infect all humans?

# Example:
#   Input:
#   [[0, 1, 1, 0, 1],
#    [0, 1, 0, 1, 0],
#    [0, 0, 0, 0, 1],
#    [0, 1, 0, 0, 0]]

# Output: 2
# Explanation:
#   At the end of the 1st hour, the status of the grid:
#   [[1, 1, 1, 1, 1],
#    [1, 1, 1, 1, 1],
#    [0, 1, 0, 1, 1],
#    [1, 1, 1, 0, 1]]
#   At the end of the 2nd hour, the status of the grid:
#   [[1, 1, 1, 1, 1],
#    [1, 1, 1, 1, 1],
#    [1, 1, 1, 1, 1],
#    [1, 1, 1, 1, 1]]
# int minHours(int rows, int columns, List < List < Integer >> grid) {
# 	// todo
# }
from typing import List
class Solution:
    def minHours(self, rows:int, columns:int, grid:List[List[int]]) -> int:
        minHoursToInfectAll = 0
        totalArea = rows * columns

        # handle poor input parameters
        if not grid or len(grid) == 0 or len(grid) == 1 and len(grid[0]) == 0:
            print('invalid input')
            return None
        if not rows or rows == 0:
            print('invalid input')
            return None
        if not columns or columns == 0:
            print('invalid input')
            return None

        print("-- starting zombies --")
        for row in range(rows):
            for col in range(columns):
                # print("col[%d]row[%d]" %(col, row))
                print("%s" % grid[row][col], end=' ')
            print('\n')

        # zombieCount = 0
        while True:
            zombieCount = 0
            zombieLocations = []
            for row in range(rows):
                for col in range(columns):
                    if grid[row][col] == 1:
                        # print("found zombie at [%d][%d]" % (row,col))
                        zombieLocations.append([row,col])
                        zombieCount += 1
            if zombieCount == totalArea:
                break
            
            # handle 1hr outbreak 
            while (zombieLocations):
                currentZombie = zombieLocations.pop()
                row = currentZombie[0]
                col = currentZombie[1]

                if (row - 1 >= 0) and (grid[row - 1][col] == 0):
                    grid[row - 1][col] = 1
                if (row + 1 < rows) and (grid[row +1][col] == 0):
                    grid[row + 1][col] = 1
                if (col - 1 >= 0) and (grid[row][col - 1] == 0):
                    grid[row][col - 1] = 1
                if (col + 1 < columns) and (grid[row][col + 1] == 0):
                    grid[row][col + 1] = 1
            
            minHoursToInfectAll += 1
            if (minHoursToInfectAll > 5):
                break
                            
            print("-- after hour %d --" % (minHoursToInfectAll))
            for row in range(rows):
                for col in range(columns):
                    print("%s" % grid[row][col], end=' ')
                print('\n')

        return minHoursToInfectAll

s = Solution()
input = [[0, 1, 1, 0, 1],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0]]
solution = 2
output = s.minHours(len(input), len(input[0]), input)
print("%s | output = %s" % (output == solution, output))
