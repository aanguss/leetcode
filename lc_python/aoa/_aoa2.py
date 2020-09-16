# 
from typing import List


def foo(itemAssociation):
    if len(itemAssociation < 1):
        return itemAssociation

    fullDictionary = {}
    # add input string pairs to dictionary of list values
    for item in itemAssociation:
        if item in fullDictionary:
            fullDictionary[item] += 1
        else:
            fullDictionary.update({item: [1]})

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
                    for item not in visitList:
                        stackList.append(item)
        visitList.sort()
        fullListOfLists.append(visitList)

    fullListOfLists.sort(key=len, reverse=True)

    return fullListOfLists[0]


# psList = []
# ps1 = PairString()
# ps1.PairString("item1", "item2")
# ps2 = PairString()
# ps2.PairString("item3", "item4")
# ps3 = PairString()
# ps3.PairString("item4", "item5")
# psList.append(ps1)
# psList.append(ps2)
# psList.append(ps3)
# ps4 = PairString()
# ps4.PairString("item1", "item3")
# psList.append(ps4)
# ps5 = PairString()
# ps5.PairString("item2", "item3")
# psList.append(ps5)

# s = Solution()
# largestList = s.largestItemAssociation(psList)
# print("longest association = %s" % largestList)
