# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/558/week-5-september-29th-september-30th/3477/
# https://leetcode.com/problems/word-break/
#
# Word Break
# Given a non-empty string s and a dictionary wordDict containing a list of 
# non-empty words, determine if s can be segmented into a space-separated 
# sequence of one or more dictionary words.
#
# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
#
# Example 1:
#     Input: s = "leetcode", wordDict = ["leet", "code"]
#     Output: true
#     Explanation: Return true because "leetcode" can be segmented as "leet code".
#
# Example 2:
#     Input: s = "applepenapple", wordDict = ["apple", "pen"]
#     Output: true
#     Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#                 Note that you are allowed to reuse a dictionary word.
#
# Example 3:
#     Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
#     Output: false
from typing import List
import timeit
import itertools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        debug = False
        if debug: print(s)
        queue = []
        visited = []
        queue.append(0)
        while queue:
            left = queue.pop()
            if left not in visited:
                visited.append(left)
                for right in range(left + 1, len(s) + 1):
                    if debug: print('testing:', s[left:right])
                    if s[left:right] in wordDict:
                        if debug: print('found:', s[left:right])
                        queue.append(right)
                        if right == len(s):
                            return True
        return False

s = Solution()
testCounts = 1
sinput = "leetcode"
wordDict = ["leet", "code"]
solution = True
output = s.wordBreak(sinput, wordDict)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))
if (output == solution):
    time = timeit.timeit(lambda: s.wordBreak(sinput, wordDict), number=testCounts)/testCounts
    print("timeit =", time)

sinput = "applepenapple"
wordDict = ["apple", "pen"]
solution = True
output = s.wordBreak(sinput, wordDict)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))
if (output == solution):
    time = timeit.timeit(lambda: s.wordBreak(sinput, wordDict), number=testCounts)/testCounts
    print("timeit =", time)

sinput = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
solution = False
output = s.wordBreak(sinput, wordDict)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))
if (output == solution):
    time = timeit.timeit(lambda: s.wordBreak(sinput, wordDict), number=testCounts)/testCounts
    print("timeit =", time)

sinput = "cbca"
wordDict = ["bc","ca"]
solution = False
output = s.wordBreak(sinput, wordDict)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))
if (output == solution):
    time = timeit.timeit(lambda: s.wordBreak(sinput, wordDict), number=testCounts)/testCounts
    print("timeit =", time)

sinput = "catskicatcats"
wordDict = ["cats","cat","dog","ski"]
solution = True
output = s.wordBreak(sinput, wordDict)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))
if (output == solution):
    time = timeit.timeit(lambda: s.wordBreak(sinput, wordDict), number=testCounts)/testCounts
    print("timeit =", time)