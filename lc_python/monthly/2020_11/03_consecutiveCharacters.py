# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3518/
# https://leetcode.com/problems/consecutive-characters/
#
# Given a string s, the power of the string is the maximum length of a non-empty 
# substring that contains only one unique character.
#
# Return the power of the string.
#
# Example 1:
#     Input: s = "leetcode"
#     Output: 2
#     Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:
#     Input: s = "abbcccddddeeeeedcba"
#     Output: 5
#     Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
# Example 3:
#     Input: s = "triplepillooooow"
#     Output: 5
# Example 4:
#     Input: s = "hooraaaaaaaaaaay"
#     Output: 11
# Example 5:
#     Input: s = "tourist"
#     Output: 1
# Constraints:
#     1 <= s.length <= 500
#     s contains only lowercase English letters.

class Solution:
    def maxPower(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        maxString = ""
        currentString = s[0]

        i = 1
        while True:
            print(s[i])
            if s[i] == s[i-1]:
                currentString += s[i]
            else:
                if len(currentString) > len(maxString):
                    maxString = currentString
                    print(maxString)
                currentString = s[i]
            i += 1
            if i >= len(s):
                if len(currentString) > len(maxString):
                    maxString = currentString
                break

        return len(maxString)

        ##### WRONG METHOD - Returned max chars is all #####
        # charDict = {}
        # maxS = ""

        # for i in range(len(s)):
        #     if s[i] in charDict:
        #         charDict[s[i]] += s[i]
        #     else:
        #         charDict[s[i]] = s[i]
        # print(charDict)
        # maxS = sorted(charDict.items(), key=lambda x:len(x[1]), reverse=True)[0][1]
        # print(maxS)

        # return maxS

s = Solution()
inputString = "leetcode"
solution = 2
output = s.maxPower(inputString)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

inputString = "triplepillooooow"
solution = 5
output = s.maxPower(inputString)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))
