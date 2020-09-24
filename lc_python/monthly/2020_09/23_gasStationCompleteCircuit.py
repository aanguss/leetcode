# https://leetcode.com/problems/gas-station/
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3470/
#
# There are N gas stations along a circular route, where the amount of gas at 
# station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to 
# travel from station i to its next station (i+1). You begin the journey with 
# an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit 
# once in the clockwise direction, otherwise return -1.
#
# Note:
# If there exists a solution, it is guaranteed to be unique.
# Both input arrays are non-empty and have the same length.
# Each element in the input arrays is a non-negative integer.
#
# Example 1:
#     Input: 
#         gas  = [1,2,3,4,5]
#         cost = [3,4,5,1,2]
#     Output: 
#         3
#     Explanation:
#         Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
#         Travel to station 4. Your tank = 4 - 1 + 5 = 8
#         Travel to station 0. Your tank = 8 - 2 + 1 = 7
#         Travel to station 1. Your tank = 7 - 3 + 2 = 6
#         Travel to station 2. Your tank = 6 - 4 + 3 = 5
#         Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
#         Therefore, return 3 as the starting index.
#
# Example 2:
#     Input: 
#         gas  = [2,3,4]
#         cost = [3,4,3]
#     Output: 
#         -1
#     Explanation:
#         You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
#         Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
#         Travel to station 0. Your tank = 4 - 3 + 2 = 3
#         Travel to station 1. Your tank = 3 - 3 + 3 = 3
#         You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
#         Therefore, you can't travel around the circuit once no matter where you start.
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        debug = False
        totalStations = len(gas)
        currentStation = 0
        stationAnswer = -1
        
        for startingStation in range(totalStations):
            if debug: print("-----starting station =", startingStation)
            if gas[startingStation] < cost[startingStation]:
                continue
            gasTank = 0
            completedCircuit = True
            for i in range(startingStation, startingStation + totalStations + 1, 1):
                currentStation = i % totalStations
                gasTank += gas[currentStation]
                gasCost = cost[currentStation]
                gasTank -= gasCost

                if debug: print("currentStation =", currentStation)
                if debug: print("gasTank =", gasTank)
                if debug: print("gasCost =", gasCost)

                if gasTank < 0:
                    if debug: print("ran out of gas :(")
                    completedCircuit = False
                    break
            if completedCircuit:
                stationAnswer = startingStation
                break

        return stationAnswer
# SUPER SLOW SOLUTION :(
        # debug = False
        # totalStations = len(gas)
        # currentStation = 0
        # startingStation = 0
        # # stationFound = False
        # while True:
        #     # gasTank = gas[(startingStation - 1) % totalStations]
        #     gasTank = gas[startingStation]
        #     completedCircuit = True
        #     if debug: print("-----starting station =", startingStation)

        #     # for i in range(startingStation + 1, startingStation + totalStations + 1, 1):
        #     currentStation = startingStation
        #     visitedStations = 0
        #     if gas[startingStation] < cost[startingStation]:
        #         validStationTest = False
        #         # completedCircuit = False
        #     else:
        #         validStationTest = True
        #     # while validStationTest:
        #     for i in range(startingStation, startingStation + totalStations + 1, 1):
        #         # if debug: print("i =", i)
        #         currentStation = i % totalStations
        #         gasCost = cost[currentStation]

        #         if debug: print("currentStation =", currentStation)
        #         if debug: print("gasCost =", gasCost)
        #         if debug: print("gasTank =", gasTank)

        #         # can't be this iteration because ran out of gas
        #         if ((gasTank - gasCost) < 0):
        #             if debug: print("ran out of gas :(")
        #             completedCircuit = False
        #             break
        #         # else:
        #         gasTank -= gasCost
        #         currentStation = (currentStation + 1) % totalStations
        #         gasTank += gas[currentStation]
        #         visitedStations += 1
        #         if visitedStations > totalStations:
        #             # stationFound = True
        #             break
        #     if completedCircuit and validStationTest:
        #         break
        #     else:
        #         startingStation += 1

        #     if startingStation >= totalStations:
        #         startingStation = -1
        #         break

        # return startingStation

s = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
solution = 3
output = s.canCompleteCircuit(gas, cost)
print("%s | %s" % ('PASS' if output == solution else 'FAIL', output))

gas  = [2,3,4]
cost = [3,4,3]
solution = -1
output = s.canCompleteCircuit(gas, cost)
print("%s | %s" % ('PASS' if output == solution else 'FAIL', output))

gas  = [5,8,2,8]
cost = [6,5,6,6]
solution = 3
output = s.canCompleteCircuit(gas, cost)
print("%s | %s" % ('PASS' if output == solution else 'FAIL', output))