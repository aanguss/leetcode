# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2975/
# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it is able to trap after raining.
#####
# Example
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not len(height) > 1:
            return 0

        highPoint = 0
        indexNextHighPoint = 0
        canHoldWater = True
        totalWater = 0

        for i in range(len(height)):
            if height[i] >= highPoint or i == indexNextHighPoint:
                highPoint = height[i]

                # get next highest point that can contain water
                indexNextHighPoint = i
                if (i + 1 < len(height)):
                    tempI = i + 1
                    while indexNextHighPoint == i:
                        if (tempI + 1 < len(height)):
                            tempI += 1

                            if height[tempI] >= highPoint:
                                indexNextHighPoint = tempI
                        else:
                            tempI = i + 1
                            highPoint -= 1
                            if highPoint == -1:
                                return totalWater
            else:
                if (height[i] < highPoint and height[i] < height[indexNextHighPoint]):
                    if highPoint <= height[indexNextHighPoint]:
                        totalWater += highPoint - height[i]
                    else:
                        totalWater += height[indexNextHighPoint] - height[i]
            
        return totalWater
            


s = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
totalWater = s.trap(input)
print("total water = " + str(totalWater))