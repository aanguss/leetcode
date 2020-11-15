# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3528/
# https://leetcode.com/problems/permutations-ii/
#
# Given a collection of numbers, nums, that might contain duplicates, return all 
# possible unique permutations in any order. 
#
# Example 1:
#     Input: nums = [1,1,2]
#     Output:
#     [[1,1,2],
#     [1,2,1],
#     [2,1,1]]
# Example 2:
#     Input: nums = [1,2,3]
#     Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Constraints:
#     1 <= nums.length <= 8
#     -10 <= nums[i] <= 10
#
from typing import List
class Solution:
    superList = []
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums == None or len(nums) == 0:
            return [[]]
        global newList 
        newList = []
        uniqueList = list(dict.fromkeys(nums))
        
        # for i in range(len(uniqueList)):
        #     subList = []
        #     for j in range(len(uniqueList)):
        #         j += (i+1)
        #         if j >= len(uniqueList):
        #             j -= len(uniqueList)
        #         subList.append(uniqueList[j])
        #     newList.append(subList)
        # print(newList)
        
        # for i in range(len(uniqueList)):
        #     subList = []
        #     subList.append(uniqueList[i])
        #     for j in range(i,len(uniqueList)):
        #         subList.append(uniqueList[j])
        #     newList.append(subList)
        # print(newList)

        # for i in range(len(nums)):
        #     subList = []
        #     for j in range

        # for i in range(2):
        #     subList = []
        #     # print(i, end=': ')
        #     for j in range(3):
        #         # print(j, end=' ')
        #     print('\n')
        
        # for a in nums:
        #     for b in nums:
        #         for c in nums:
        #             print(a,b,c) 

        # for a in uniqueList:
        #     for b in uniqueList:
        #         for c in uniqueList:
        #             if (a != b and a != c and b != c):
        #                 print(a,b,c)

        # https://www.geeksforgeeks.org/python-program-to-print-all-permutations-of-a-given-string/

        def bigPerm(a, l, r, n=None):
            if l == r: 
                print(a)
                if n == None:
                    n = []
                n.append(a)
            else: 
                for i in range(l, r + 1): 
                    a[l], a[i] = a[i], a[l] 
                    bigPerm(a, l + 1, r, n) 
                    a[l], a[i] = a[i], a[l] # backtrack
        bigPerm(nums, 0, len(nums) - 1, newList)
       
        print('newlist')
        print(newList)

        # newUList = []
        # for i in newList:
        #     if i not in newUList:
        #         newUList.append(i)

        # aUniqueList = list(dict.fromkeys(newList))

        # print(aUniqueList)
        # print('newUList = ')
        # print(newUList)

        return newList

s = Solution()
nums = [1,1,2]
solution = [[1,1,2],[1,2,1],[2,1,1]]
output = s.permuteUnique(nums)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# nums = [1,2,3]
# solution = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# output = s.permuteUnique(nums)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))