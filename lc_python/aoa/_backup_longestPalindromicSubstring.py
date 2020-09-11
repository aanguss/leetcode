# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, find the longest palindromic substring in s. You may 
# assume that the maximum length of s is 1000.

# Example 1:
#     Input: "babad"
#     Output: "bab"
#     Note: "aba" is also a valid answer.
# Example 2:
#     Input: "cbbd"
#     Output: "bb"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPal = ""
        listOfPals = []

        if s == None or s == '':
            return ""
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                subPal = []
                foundMatch = False
                matchedAllK = True
                if s[i] == s[j]:
                    for k in range(0, j - i):
                        if s[i + k] == s[j - k]:
                            # print("matches:", s[i:j+1])
                            subPal = s[i:j+1]
                            foundMatch = True
                        else:
                            matchedAllK = False
                if matchedAllK and foundMatch:
                    if subPal not in listOfPals:
                        listOfPals.append(subPal)
        # print(listOfPals)
        if len(listOfPals) < 1:
            if len(s) < 2:
                return ''
            else:
                return s[0]
        else:
            longestPal = max(listOfPals, key=len)

        return longestPal


s = Solution()
input = "babad"
solution = "bab"
output = s.longestPalindrome(input)
print("%s | %s" % ("PASS" if (output == solution) else "FAIL", output))

input = "cbbd"
solution = "bb"
output = s.longestPalindrome(input)
print("%s | %s" % ("PASS" if (output == solution) else "FAIL", output))

input = "abcda"
solution = "a"
output = s.longestPalindrome(input)
print("%s | %s" % ("PASS" if (output == solution) else "FAIL", output))
