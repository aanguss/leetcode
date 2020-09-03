# 1119. Remove Vowels from a String
# https://leetcode.com/problems/remove-vowels-from-a-string/
# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
# 
# Example 1:
#   Input: "leetcodeisacommunityforcoders"
#   Output: "ltcdscmmntyfrcdrs"
# Example 2:
#   Input: "aeiou"
#   Output: ""
# Note:
#   S consists of lowercase English letters only.
#   1 <= S.length <= 1000

class Solution:
    def removeVowels(self, fullString: str) -> str:
        vowels = "aeiou"
        for vowel in vowels:
            fullString = fullString.replace(vowel,'')

        return fullString

s = Solution()
inputString = "leetcodeisacommunityforcoders"
outputString = s.removeVowels(inputString)
print("output1 is '%s'" % (outputString))

inputString = "aeiou"
outputString = s.removeVowels(inputString)
print("output2 is '%s'" % (outputString))

val = "ab"
outputString3 = "abcdefg"
print(outputString3.replace(val[0],""))