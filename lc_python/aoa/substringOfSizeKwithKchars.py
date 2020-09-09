# https: // leetcode.com/discuss/interview-question/370112
# Given a string s and an int k, return all unique substrings of s of size k 
# with k distinct characters.
# 
# Example 1:
#   Input: s = "abcabc", k = 3
#   Output: ["abc", "bca", "cab"]
# 
# Example 2:
#   Input: s = "abacab", k = 3
#   Output: ["bac", "cab"]
# 
# Example 3:
#   Input: s = "awaglknagawunagwkwagl", k = 4
#   Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu",
#            "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
# Explanation:
#   Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", 
#                       "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl"
#   "wagl" is repeated twice, but is included in the output once.
# 
# Constraints:
#   The input string consists of only lowercase English letters[a-z]
#   0 ≤ k ≤ 26
from typing import List
class Solution:
    def getSubStringK(self, inputString: str, inputSize: int) -> List[str]:
        print("starting string = %s and k = %d" % (inputString, inputSize))
        subStringList = []
        

        
        for i in range(len(inputString) - inputSize + 1):
            newSubString = ''
            # print("testing -> inputString[%d] = %s" % (i, inputString[i : i + inputSize]))
            for j in range(i, i + inputSize):
                # print("looking for %s in %s" % (inputString[j], inputString[j : i + inputSize]))
                try:
                    if(inputString.index(inputString[j], j + 1, i + inputSize)):
                        newSubString = ''
                        # print("found repeat - going to next")
                        break
                except:
                    newSubString = inputString[i : i + inputSize]
                    
            # print(newSubString)
            if newSubString:
                try:
                    if subStringList.index(newSubString):
                        continue
                except:
                    subStringList.append(newSubString)

        
        return subStringList

s = Solution()
stringList = s.getSubStringK('abcabc', 3)
solution = ["abc", "bca", "cab"]
print("%s - %s\n" % (stringList == solution, stringList))

stringList = s.getSubStringK('abacab', 3)
solution = ["bac", "cab"]
print("%s - %s\n" % (stringList == solution, stringList))

stringList = s.getSubStringK('awaglknagawunagwkwagl', 4)
solution = ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
print("%s - %s\n" % (stringList == solution, stringList))
