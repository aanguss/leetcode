# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/
# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.  
# The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  
# The digit-logs should be put in their original order.
#
# Return the final order of the logs.
#
# Example 1:
#     Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#     Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
#
# Constraints:
#     0 <= logs.length <= 100
#     3 <= logs[i].length <= 100
#     logs[i] is guaranteed to have an identifier, and a word after the identifier.
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []
        newLogs = []
        
        for log in logs:
            logSplit = log.split()
            # print(logSplit[0], logSplit[1])
            if not logSplit[1].isdigit():
                # print("found letter")
                letterLogs.append(log.split())
            else:
                # print("found digit")
                digitLogs.append(log)
        
        if letterLogs:
            # print(letterLogs)
            letterLogsSorted = []
            # first sort lexiwhateverish
            letterLogs.sort()
            # now sort with 2nd index and on
            letterLogs.sort(key = lambda x: x[1:])
            for log in letterLogs:
                log = " ".join(log)
                letterLogsSorted.append(log)
            # print(letterLogsSorted)
            
            newLogs.extend(letterLogsSorted)

        if digitLogs:
            newLogs.extend(digitLogs)

        return newLogs

s = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
answer = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
output = s.reorderLogFiles(logs)
print(output)
print(output == answer)


logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
answer = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
output = s.reorderLogFiles(logs)
print(output)
print(output == answer)

logs = ["t kvr", "r 3 1", "i 403", "7 so", "t 54"]
answer = ["t kvr", "7 so", "r 3 1", "i 403", "t 54"]
output = s.reorderLogFiles(logs)
print(output)
print(output == answer)
