# https://leetcode.com/problems/car-pooling/
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3467/
# Car Pooling
# You are driving a vehicle that has capacity empty seats initially available 
# for passengers.  The vehicle only drives east (ie. it cannot turn around 
# and drive west.)
#
# Given a list of trips, trip[i] = [num_passengers, start_location, end_location]
# contains information about the i-th trip: the number of passengers that must 
# be picked up, and the locations to pick them up and drop them off.  The 
# locations are given as the number of kilometers due east from your vehicle's 
# initial location.
#
# Return true if and only if it is possible to pick up and drop off all 
# passengers for all the given trips. 
#
# Example 1:
# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
#
# Example 2:
# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
#
# Example 3:
# Input: trips = [[2,1,5],[3,5,7]], capacity = 3
# Output: true
#
# Example 4:
# Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
# Output: true
#
# Constraints:
# trips.length <= 1000
# trips[i].length == 3
# 1 <= trips[i][0] <= 100
# 0 <= trips[i][1] < trips[i][2] <= 1000
# 1 <= capacity <= 100000
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #### MUCH BETTER METHOD ####
        # timestamp = [0] * 1001
        # for trip in trips:
        #     timestamp[trip[1]] += trip[0]
        #     timestamp[trip[2]] -= trip[0]
        #
        # used_capacity = 0
        # for passenger_change in timestamp:
        #     used_capacity += passenger_change
        #     if used_capacity > capacity:
        #         return False
        # return True

        debug = True
        carPoolingPossible = True
        availableCapacity = capacity
        availableStops = 1000

        currentTripNumber = 0
        currentPassengers = []

        # sort trips by pick up
        if debug: print(trips)
        trips.sort(key = lambda x: x[1])
        if debug: print(trips)

        for i in range(availableStops):
            if debug: print("%d. " % i)

            # remove passengers ready to get off
            if debug: print(currentPassengers)
            for k in range(len(currentPassengers) - 1, -1, -1):
                passengerDropOff = currentPassengers[k][2]
                passengerCount = currentPassengers[k][0]
                if debug: print('passengerDropOff[%d] = %d' % (k, passengerDropOff))
                if passengerDropOff == i:
                    availableCapacity += passengerCount
                    if debug: print("removing passengerDropOff index", k)
                    currentPassengers.pop(k)
            if debug: print(currentPassengers)

            # see if any passengers are getting picked up
            for j in range(currentTripNumber, len(trips), 1):
                passengers = trips[j][0]
                pickup = trips[j][1]
                # dropOff = trips[j][2]

                if pickup > i:
                    if debug: print("found trip %d with pickup %d > %d" % (currentTripNumber, pickup, i))
                    break
                elif pickup < i:
                    if debug: print("found west pickup no longer valid")
                    return False
                elif pickup == i:
                    if debug: print("found trip %d with pickup %d == %d" % (currentTripNumber, pickup, i))
                    currentTripNumber += 1
                    if debug: print("availableCapacity(%d) - passengers(%d) >= 0? %s" % (availableCapacity, passengers, availableCapacity - passengers >= 0))
                    if availableCapacity - passengers >= 0:
                        currentPassengers.append(trips[j])
                        if debug: print(currentPassengers)
                        availableCapacity -= passengers
                    else:
                        return False

                if debug: print(currentTripNumber)
                if debug: print(currentPassengers)
            if currentPassengers == [] and currentTripNumber >= len(trips) - 1:
                if debug: print("found end of trips and no more passengers")
                break

        return carPoolingPossible

s = Solution()
# input = [[2,1,5],[3,3,7]]
# capacity = 4
# solution = False
# output = s.carPooling(input, capacity)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# input = [[2,1,5],[3,3,7]]
# capacity = 5
# solution = True
# output = s.carPooling(input, capacity)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# input = [[2,1,5],[3,5,7]]
# capacity = 3
# solution = True
# output = s.carPooling(input, capacity)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# input = [[3,2,7],[3,7,9],[8,3,9]]
# capacity = 11
# solution = True
# output = s.carPooling(input, capacity)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# input = [[5,4,7],[7,4,8],[4,1,8]]
# capacity = 17
# solution = True
# output = s.carPooling(input, capacity)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# input = [[7,5,6],[6,7,8],[10,1,6]]
# capacity = 16
# solution = False
# output = s.carPooling(input, capacity)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

input = [[12,93,896],[77,291,904],[78,424,659],[41,668,962],[79,2,493],[7,369,840],[60,229,928],[41,7,163],[46,621,736],[97,958,984],[53,832,980],[15,218,815],[24,74,428],[12,415,959],[20,81,85],[45,567,601],[17,266,535],[65,828,943],[30,416,432],[27,48,142],[52,413,756],[21,79,274],[4,260,387],[49,180,314],[51,628,880],[94,271,462],[41,163,457],[30,187,925],[39,349,999],[5,289,809],[9,214,374],[10,302,534],[59,412,778],[77,306,497],[17,594,839],[53,404,892],[5,525,844],[89,275,619],[2,27,310],[79,473,755],[10,812,853],[76,55,549],[100,643,770],[36,701,997],[59,354,475],[70,586,924],[60,146,972],[32,121,305],[27,75,132],[17,32,758],[24,389,465],[81,55,258],[70,74,728],[36,184,703],[66,603,853],[63,319,964],[15,355,676],[69,312,521],[83,344,995],[41,73,439],[28,384,758],[90,341,365],[11,473,980],[49,631,737],[6,116,531],[99,334,460],[78,358,508],[26,426,823],[10,312,677],[48,532,711],[64,433,635],[62,591,765],[100,150,837],[24,60,945],[6,72,237],[21,602,838],[75,255,629],[54,824,935],[53,169,263],[49,401,744],[1,603,922],[88,284,984],[25,896,998],[13,379,493],[2,293,295],[31,106,600],[91,284,631],[42,16,880],[89,62,803],[96,168,279],[8,731,902],[44,348,755],[68,462,537],[96,694,913],[51,190,651],[7,92,179],[91,5,65],[14,338,818],[98,423,953],[15,636,664]]
capacity = 2637
solution = False
output = s.carPooling(input, capacity)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))