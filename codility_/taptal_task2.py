# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    tripLocations = []
    locationsVisited = []
    tripDuration = 0
    shortestTrip = 0

    # if there is only one destination, return only that
    if len(A) == 1:
        return 1

    # find all the available trip locations
    for i in range(len(A)):
        if A[i] not in tripLocations:
            tripLocations.append(A[i])
    # print(tripLocations)

    # go backwards from the end of the trip and find when all locations visited
    for i in range(len(A) - 1, -1, -1):
        # keep track of when a new location has been visisted
        if A[i] in tripLocations and A[i] not in locationsVisited:
            locationsVisited.append(A[i])
            shortestTrip = i
        # stop lookign once all locations have been found
        if len(tripLocations) == len(locationsVisited):
            shortestTrip = i
            break

    # calculate trip duration with the - 1 to account for the 0 index
    tripDuration = len(A) - shortestTrip - 1

    return tripDuration


print(solution([7, 3, 7, 3, 1, 3, 4, 1]))
# Example test:   [7, 3, 7, 3, 1, 3, 4, 1]
# OK

# Example test:   [2, 1, 1, 3, 2, 1, 1, 3]
# OK

# Example test:   [7, 5, 2, 7, 2, 7, 4, 7]
# OK
