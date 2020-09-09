# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2973/
# Given a paragraph and a list of banned words, return the most frequent word that is not 
# in the list of banned words.  It is guaranteed there is at least one word that isn't banned, 
# and that the answer is unique.
# 
# Words in the list of banned words are given in lowercase, and free of punctuation.  Words 
# in the paragraph are not case sensitive.  The answer is in lowercase.
####
# Example
# Input: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.

from typing import List
debugPrint = False
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        wordDict = {}
        highestValue = 0
        highestKey = ''
        splitParagraph = paragraph.lower().replace(",", " ").replace(".","").replace("!","").replace("?","").replace("'","").replace(";","")
        splitParagraph = splitParagraph.split()
        
        for word in splitParagraph:
            if debugPrint: print(word)
            if word in wordDict.keys() :
                wordDict[word] += 1
            else:
                wordDict.update({word.lower(): 1})

        if debugPrint: print(wordDict)

        for ban in banned:
            if ban in wordDict.keys() :
                del wordDict[ban]

        if debugPrint: print(wordDict)
        for key in wordDict:
            if wordDict[key] > highestValue:
                highestValue = wordDict[key]
                highestKey = key

        if debugPrint: print(highestKey)
        return highestKey

s = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
mostCommon = s.mostCommonWord(paragraph, banned)
print(mostCommon)

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
mostCommon = s.mostCommonWord(paragraph, banned)
print(mostCommon)