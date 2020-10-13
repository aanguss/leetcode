# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3492/
# https://leetcode.com/problems/buddy-strings/
#
# Given two strings A and B of lowercase letters, return true if you can swap two 
# letters in A so the result is equal to B, otherwise, return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed) such that 
# i != j and swapping the characters at A[i] and A[j]. For example, swapping at 
# indices 0 and 2 in "abcd" results in "cbad".
#
# Example 1:
#     Input: A = "ab", B = "ba"
#     Output: true
#     Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", 
#         which is equal to B.
#
# Example 2:
#     Input: A = "ab", B = "ab"
#     Output: false
#     Explanation: The only letters you can swap are A[0] = 'a' and 
#         A[1] = 'b', which results in "ba" != B.
#
# Example 3:
#     Input: A = "aa", B = "aa"
#     Output: true
#     Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", 
#         which is equal to B.
#
# Example 4:
#     Input: A = "aaaaaaabc", B = "aaaaaaacb"
#     Output: true
#
# Example 5:
#     Input: A = "", B = "aa"
#     Output: false
#
# Constraints:
#     0 <= A.length <= 20000
#     0 <= B.length <= 20000
#     A and B consist of lowercase letters.
from typing import List
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        stringsMatch = False
        pos1 = None
        pos2 = None
        newA = ""

        if A is None or len(A) == 0:
            return False
        if B is None or len(B) == 0:
            return False
        if len(A) - len(B) > abs(2):
            return False

        for i in range(len(A)):
            if (A[i] != B[i]):
                if pos1 is None:
                    pos1 = i
                elif pos2 is None:
                    pos2 = i
        
        # if pos1 != None and pos2 != None:
        #     print("A[%d] = %s and A[%s] = %s" % (pos1, A[pos1], pos2, A[pos2]))

        if pos1 == None and pos2 == None:
            for i in range(len(A)):
                x = A[::-1].index(A[i])
                if (x != -1):
                    if (len(A) - x - 1 == i):
                        continue
                    else:
                        pos1 = i
                        pos2 = len(A) - x - 1
                        # print("x = %s and found pos1 = %s and pos2 = %s" % (x, pos1, pos2))
                        break

        if pos1 == pos2:
            return False
        if pos1 == None or pos2 == None:
            return False
        if pos1 == None and pos2 == None:
            return False

        for i in range(len(A)):
            if (i == pos1):
                newA += A[pos2]
            elif (i == pos2):
                newA += A[pos1]
            else:
                newA += A[i]

        # print("newA = %s" % newA)

        if (newA == B):
            stringsMatch = True
        
        return stringsMatch


s = Solution()
inputA = "ab"
inputB = "ba"
solution = True
output = s.buddyStrings(inputA, inputB)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

inputA = "ab"
inputB = "ab"
solution = False
output = s.buddyStrings(inputA, inputB)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

inputA = "aa"
inputB = "aa"
solution = True
output = s.buddyStrings(inputA, inputB)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

inputA = "aaaaaaabc"
inputB = "aaaaaaacb"
solution = True
output = s.buddyStrings(inputA, inputB)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

inputA = ""
inputB = "aa"
solution = False
output = s.buddyStrings(inputA, inputB)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

inputA = "abccccc"
inputB = "abccccc"
solution = True
output = s.buddyStrings(inputA, inputB)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))