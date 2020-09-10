# https: // leetcode.com/discuss/interview-question/376375/
#
# Given a list of unique integers nums, construct a BST from it(you need to insert 
# nodes one-by-one with the given order to get the BST) and find the distance 
# between two nodes node1 and node2. Distance is the number of edges between two 
# nodes. If any of the given nodes does not appear in the BST, return -1.
#
# Example 1:
#     Input: nums = [2, 1, 3], node1 = 1, node2 = 3
#     Output: 2
#     Explanation:
#         2
#       /   \
#      1     3
from typing import List
class Solution:
    def getDistanceBetweenNodes(self, nums: List[int], node1: int, node2: int) -> int:
        

        return -1

s = Solution()
nums = [2, 1, 3]
node1 = 1
node2 = 3
solution = 2
output = s.getDistanceBetweenNodes(nums, node1, node2)
print("%s | %s" % (output == solution, output))