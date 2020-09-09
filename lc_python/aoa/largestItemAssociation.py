# https://leetcode.com/discuss/interview-question/782606/
# In order to improve customer experience, Amazon has developed a system to 
# provide recommendations to the customers regarding the items they can 
# purchase.  Based on historical customer purchase information, an item
# association can be deinfed as - if an item A is ordered by a customer, then
# item B is also likely to be ordered by the same customer (e.g. Book 1 is
# frequenctly ordered with Book 2).  All items that are linked together by an
# item association can be considered to be in teh same group.  An item without
# any association to any other item can be considered to be in its own item
# association group of size 1.

# Given a list of item associtaion relationships (i.e. group of items likely
# to be ordered together), write an algorithm that outputs the largest item
# association group.  If two groups have the same number of items then select
# the group which contains the item that appears first in lexicographic order.

# Input
# The input to the functin/method consists of an argument - itemAssociation, a
# list containing pairs of strings representing the items that are ordered together.

# Output
# Return a list of strings representing the largest item association group,
# sorted lexicographically.

# Example
# Input, itemAssociation = [[item1, item2], [item3, item4], [item4, item5]]
# Output, [item3, item4, item5]

# Explanation
# There are two item association groups
#   group1: [item1, item2]
#   group2: [item3, item4, item5]
# In the available item associations, group2 has the largest association.  So
# the output is [item3, item4, item5]

# Helper Description
# The following class is used to represent a Pair of strings and is already
# implmented in the default code (Do not write this definition again in your code):
# class PairString:
#     first = ""
#     second = ""
#     def PairString(self, first: str, second: str):
#         self.first = first
#         self.second = second
from typing import List
class PairString:
    first = ""
    second = ""
    def PairString(self, first: str, second: str):
        self.first = first
        self.second = second

class Solution:
    def largestItemAssociation(self, itemAssociation: List[PairString]) -> List[str]:

        if len(itemAssociation < 1):
            return itemAssociation
            
        fullDictionary = {}
        # add input string pairs to dictionary of list values 
        for item in itemAssociation:
            if item.first in fullDictionary:
                fullDictionary.update({item.first:fullDictionary[item.first] + [item.second]})
            else:
                fullDictionary.update({item.first:[item.second]})
        print("staring input = %s" % fullDictionary)

        fullListOfLists = []
        for key in fullDictionary:
            stackList = []
            visitList = []
            stackList.append(key)

            while stackList:
                currentKey = stackList.pop()

                if currentKey not in visitList:
                    visitList.append(currentKey)

                if currentKey in fullDictionary:
                    for item in fullDictionary[currentKey]:
                        if item not in visitList:
                            stackList.append(item)
            visitList.sort()
            fullListOfLists.append(visitList)

        fullListOfLists.sort(key=len, reverse=True)
        
        return fullListOfLists[0]

psList = []
ps1 = PairString()
ps1.PairString("item1", "item2")
ps2 = PairString()
ps2.PairString("item3", "item4")
ps3 = PairString()
ps3.PairString("item4", "item5")
psList.append(ps1)
psList.append(ps2)
psList.append(ps3)
ps4 = PairString()
ps4.PairString("item1", "item3")
psList.append(ps4)
ps5 = PairString()
ps5.PairString("item2", "item3")
psList.append(ps5)

s = Solution()
largestList = s.largestItemAssociation(psList)
print("longest association = %s" % largestList)