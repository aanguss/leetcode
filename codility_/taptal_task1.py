# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(T, R):
    # write your code in Python 3.6
    totalScore = 0
    testNumberIndex = 0

    # find index of group number
    for i, c in enumerate(T[0]):
        if c.isdigit():
            testNumberIndex = i
            break

    # dictionary to track results
    groupTrack = {}
    for i in range(len(T)):
        if T[i][testNumberIndex] not in groupTrack:
            groupTrack[T[i][testNumberIndex]] = 100

    # remove failing group values
    for i in range(len(T)):
        # print(T[i])
        if R[i] == "Wrong answer" or R[i] == "Runtime error" or R[i] == "Time limit exceeded":
            groupTrack[T[i][testNumberIndex]] = 0

    # sum up the scores achieved
    totalScore = 0
    # print(groupTrack)
    for key in groupTrack:
        if groupTrack[key] == 100:
            totalScore += 100

    return int(totalScore/len(groupTrack))
