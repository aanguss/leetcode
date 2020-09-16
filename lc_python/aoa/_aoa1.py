# 

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'foo' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER flightDuration
#  2. INTEGER_ARRAY movieDuration
#
from typing import List

# function to find two movies that end 30 mins before the flight ends
# input:
#   flightDuration:int, time of flight in mins
#   movieDuration:List[int], movie times available
# return:
#   pairList:List[int], index of movies that meet criteria
#       if no pair is found, it will return [-1,-1]
def foo(flightDuration, movieDuration):
    # handle empty flight duration
    if flightDuration <= 30:
        return [-1, -1]

    # movie needs to end 30 mins before the flight ends
    target = flightDuration - 30

    # keep track of all available pairs that meet time criteria
    pairList = []

    # handle if movieDuration is empty, return empty list
    if movieDuration == None or len(movieDuration) == 0:
        return [-1, -1]

    # loop through all the movies to find which ones meet criteria
    for i in range(len(movieDuration)):
        for j in range(len(movieDuration)):
            # should not play one movie twice
            if i == j:
                continue
            if movieDuration[i] + movieDuration[j] == target:
                # only add the pair list if it's not already there
                if [i, j] not in pairList and [j, i] not in pairList:
                    pairList.append([i, j])

    # handle no movies found
    if len(pairList) == 0:
        return [-1, -1]

    print(pairList)

    # find largest movie index
    largestValue = 0
    largestPairIndex = 0
    for i in range(len(pairList)):
        print(pairList)
        if movieDuration[pairList[i][0]] > largestValue:
            largestValue = movieDuration[pairList[i][0]]
            largestPairIndex = i
            print(largestValue)
        if movieDuration[pairList[i][1]] > largestValue:
            largestValue = movieDuration[pairList[i][1]]
            largestPairIndex = i
            print(largestValue)

    print(pairList[largestPairIndex])
    return pairList[largestPairIndex]


# input = [1,10,25,35,60]
# target = 90
# solution = [2,3]
# output = foo(target, input)
# print("%s | output = %s" % (output == solution, output))

# input = [250, 5, 100, 180, 40, 120, 10]
input = [100, 180, 40, 120, 10]
target = 250
solution = [1, 2]
output = foo(target, input)
print("%s | output = %s" % (output == solution, output))

# print(copyOfPairList)
# copyOfPairList.sort(key=lambda x: x[1])
# if copyOfPairList[0][1] > copyOfPairList[0][0]:
#     largestValue = copyOfPairList[0][1]
# else:
#     largestValue = copyOfPairList[0][0]
# print(copyOfPairList)
# copyOfPairList.sort(key=lambda x: x[0])
# if copyOfPairList[0][1] > copyOfPairList[0][0]:
#     if copyOfPairList[0][1] > largestValue:
#         largestValue = copyOfPairList[0][1]
# else:
#     if copyOfPairList[0][0] > largestValue:
#         largestValue = copyOfPairList[0][0]
# print(copyOfPairList)
# largestPairIndex = pairList.index(largestValue)
