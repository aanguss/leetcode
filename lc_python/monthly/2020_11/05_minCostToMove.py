# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3520/
# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
# 
# We have n chips, where the position of the ith chip is position[i].
#
# We need to move all the chips to the same position. In one step, we can 
# change the position of the ith chip from position[i] to:
#   position[i] + 2 or position[i] - 2 with cost = 0.
#   position[i] + 1 or position[i] - 1 with cost = 1.
# 
# Return the minimum cost needed to move all the chips to the same position.
#
# Example 1:
#     Input: position = [1,2,3]
#     Output: 1
#     Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
#     Second step: Move the chip at position 2 to position 1 with cost = 1.
#     Total cost is 1.
# Example 2:
#     Input: position = [2,2,2,3,3]
#     Output: 2
#     Explanation: We can move the two chips at position  3 to position 2. 
#     Each move has cost = 1. The total cost = 2.
# Example 3:
#     Input: position = [1,1000000000]
#     Output: 1
# Constraints:
#     1 <= position.length <= 100
#     1 <= position[i] <= 10^9
from typing import List
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        debug = False
        minOdd = 0
        minEven = 0

        for i in range(len(position)):
            if position[i] % 2 == 0:
                minEven += 1
            if position[i] % 2 != 0:
                minOdd += 1
        if debug: print(minOdd,minEven)
        return min(minOdd, minEven)

s = Solution()
position = [1,2,3]
solution = 1
output = s.minCostToMoveChips(position)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

position = [2,2,2,3,3]
solution = 2
output = s.minCostToMoveChips(position)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

position = [1,1000000000]
solution = 1
output = s.minCostToMoveChips(position)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))
