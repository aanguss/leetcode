# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")

# def solution(A, S):
#     # write your code in Python 3.6
#     aLen = len(A)
#     listTracker = []
#     # print(aLen)

#     for i in range(aLen):
#         # print("i = %s -" % (i))
#         subStringL = 1
#         mean = A[i]

#         # test case of single digit
#         if mean == S:
#             # print("found S")
#             if A[i] not in listTracker:
#                 listTracker.append([A[i]])

#         # check following digits
#         for j in range(i + 1, aLen, 1):
#             # print("j = %s --" % (j))
#             # mean += A[j]
#             mean = 0
#             for k in range(i, j + 1):
#                 mean += A[k]
#             mean = mean / (len(A[i:j]) + 1)
#             if (mean.is_integer()):
#                 # print("found int")
#                 mean = int(mean)
#             # print("mean = %s" % (mean))
#             if mean == S:
#                 # print("found S")
#                 if A[i:j] not in listTracker:
#                     listTracker.append(A[i:j + 1])
#         # print(listTracker)

#     if len(listTracker) > 1000000000:
#         return 1000000000
#     else:
#         return len(listTracker)


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, S):
    # write your code in Python 3.6
    aLen = len(A)
    listTracker = []

    # go through all the digits and verity sum
    for i in range(aLen):
        subStringL = 1
        mean = A[i]

        # test case of single digit currently on
        if mean == S:
            if A[i] not in listTracker:
                listTracker.append([A[i]])

        # check following digits and check mean
        for j in range(i + 1, aLen, 1):
            mean = 0
            for k in range(i, j + 1):
                mean += A[k]
            mean = mean / (len(A[i:j]) + 1)
            if (mean.is_integer()):
                mean = int(mean)
            if mean == S:
                # if its not already been identified add to list
                if A[i:j] not in listTracker:
                    listTracker.append(A[i:j + 1])

    if len(listTracker) > 1000000000:
        return 1000000000
    else:
        return len(listTracker)
