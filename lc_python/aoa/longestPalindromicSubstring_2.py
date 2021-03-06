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
        if s == None or s == '':
            return ""
        if len(s) == 1:
            return s

        longestPal = s[0]
        for i in range(len(s)):
            for j in range(len(s) - 1, i, -1):
                if s[i] == s[j]:
                    subString = s[i:j+1]
                    subStringBackwards = subString[::-1]
                    # print("substring =", subString)
                    # print("substringB =", subStringBackwards)
                    if subString == subStringBackwards:
                        # print(subString)
                        # listOfPals.append(subString)
                        if len(subString) > len(longestPal):
                            longestPal = subString

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

input = "aa"
solution = "aa"
output = s.longestPalindrome(input)
print("%s | %s" % ("PASS" if (output == solution) else "FAIL", output))

input = "ccc"
solution = "ccc"
output = s.longestPalindrome(input)
print("%s | %s" % ("PASS" if (output == solution) else "FAIL", output))

input = "aba"
solution = "aba"
output = s.longestPalindrome(input)
print("%s | %s" % ("PASS" if (output == solution) else "FAIL", output))
