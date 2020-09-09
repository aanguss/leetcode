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
# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
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
            print(logSplit[1])
            if logSplit[1] in ['0','1','2','3','4','5','6','7','8','9']:
                digitLogs.append(log)
            else:
                letterLogs.append(log)
        
        # print(letterLogs)
        # letterLogs.sort()
        # print(letterLogs)
        # digitLogs.sort()
        
        
        
        
        letterLogsSorted = []
        digitLogsSorted = []
        
        if letterLogs:
            # for log in letterLogs:
            #     letterLogsSorted.append(log.split())
                
            # print(len(letterLogsSorted))
            # print(letterLogsSorted[0])
            
            # for log in letterLogs:
            #     print(log)
            # print('\n')
            letterLogs.sort(key=len)
            
            # print(len(letterLogsSorted[0]))
            # for i in range(len(letterLogsSorted[0])):
            # for i in range(len(letterLogsSorted)): 
            # for j in range(max(len(x) for x in letterLogsSorted)):
            #     if(letterLogsSorted[0][j]):
            #         letterLogsSorted.sort(key = lambda letterLogsSorted: letterLogsSorted[0][j])
            # print(letterLogsSorted[1][1])
            
            # letterLogsSorted.sort(key = lambda letterLogsSorted: letterLogsSorted[1][1])
            # for log in letterLogs:
            #     print(log)
                
            # for i in range(min(len(x) for x in letterLogs)):
            #     letterLogs.sort(key = lambda letterLogs: letterLogs[i])
            # for i in range(len(letterLogs[0])):
            #     for j in range(len(letterLogs[0] + 1)):
            #         if 
            
                    
            for log in letterLogs:
                newLogs.append(log)
        if digitLogs:
            # print(len(digitLogs[0]))
            # print(digitLogs[0])
            # for i in range(min(len(x) for x in digitLogs)):
            #     digitLogs.sort(key = lambda digitLogs: digitLogs[i])
            # digitLogs.sort(key=len)
            for log in digitLogs:
                newLogs.append(log)
            
        return newLogs

s = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
answer = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
output = s.reorderLogFiles(logs)
print(output)
print(output == answer)