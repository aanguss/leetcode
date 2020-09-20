#!/usr/local/bin/python3.8

# https://leetcode.com/problems/sequential-digits/
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465/
# Sequential Digits
# An integer has sequential digits if and only if each digit in the number is 
# one more than the previous digit.
#
# Return a sorted list of all the integers in the range [low, high] inclusive 
# that have sequential digits. 
#
# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]
#
# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345] 
#
# Constraints:
# 10 <= low <= high <= 10^9
from typing import List
# class Solution:
    # def sequentialDigits(self, low: int, high: int) -> List[int]:
def sequentialDigits(low, high):
    outputList = []
    currentDigit = 0
    highSize = 1
    lowSize = 1
    currentSize = 1

    if not low or not high:
        return []

    # determine size of high
    tempHigh = high
    while tempHigh >= 1:
        tempHigh = tempHigh / 10
        highSize = highSize * 10
    
    # determine size of low
    tempLow = low
    while tempLow >= 1:
        tempLow = tempLow / 10
        lowSize = lowSize * 10

    # print(lowSize)
    # print(highSize)

    while currentSize <= highSize:
        
        currentDigit = 1 * currentSize
        # print("currentSize = %s" % currentSize)
        # print("currentDigit = %s" % currentDigit)

        for i in range(1,10,1):
            currentDigit = currentDigit * 10
            currentDigit = currentDigit + i
            currentDigit = currentDigit % currentSize
            # print(currentDigit)

            # we need to check current size so we don't repeat numbers
            # and we use the / 10 so that the size matches the number
            # and not just the value required by mod
            if currentDigit <= currentSize / 10:
                pass
            elif currentDigit >= low and currentDigit <= high:
                outputList.append(currentDigit)
                # print("found")
        
        currentSize = currentSize * 10
        
    outputList.sort()
    return outputList

# s = Solution
low = 100
high = 300
solution = [123,234]
# output = s.sequentialDigits(low, high)
output = sequentialDigits(low,high)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

low = 1000
high = 13000
solution = [1234,2345,3456,4567,5678,6789,12345]
# output = s.sequentialDigits(low, high)
output = sequentialDigits(low,high)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

