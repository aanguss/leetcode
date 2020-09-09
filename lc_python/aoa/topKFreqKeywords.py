# https://leetcode.com/discuss/interview-question/542597/
# Given a list of reviews, a list of keywords and an integer k. Find the most 
# popular k keywords in order of most to least frequently mentioned.

# The comparison of strings is case-insensitive.
# Multiple occurances of a keyword in a review should be considred as a single mention.
# If keywords are mentioned an equal number of times in reviews, sort alphabetically.

# Example 1:
#   Input:
#       k = 2
#       keywords = ["anacell", "cetracular", "betacellular"]
#       reviews = [
#           "Anacell provides the best services in the city",
#           "betacellular has awesome services",
#           "Best services provided by anacell, everyone should use anacell",
#       ]
#   Output:
#       ["anacell", "betacellular"]
#   Explanation:
#       "anacell" is occuring in 2 different reviews and "betacellular" is only 
#       occuring in 1 review.
# Example 2:
#   Input:
#       k = 2
#       keywords = ["anacell", "betacellular",
#             "cetracular", "deltacellular", "eurocell"]
#       reviews = [
#           "I love anacell Best services; Best services provided by anacell",
#           "betacellular has great services",
#           "deltacellular provides much better services than betacellular",
#           "cetracular is worse than anacell",
#           "Betacellular is better than deltacellular.",
#       ]
# Output:
#   ["betacellular", "anacell"]
# Explanation:
#   "betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" 
#   are occuring in 2 reviews, but "anacell" is lexicographically smaller.
from typing import List
class Solution:
    def getFrequentKeywords(self, k: int, keywords: List[str], reviews: List[str]):
        if not k: return []
        if not keywords: return []
        if not reviews: return []

        keywordDictionary = {}
        # maxValues = []
        # set all keywords and reviews to lowercase
        keywords = [x.lower() for x in keywords]
        reviews = [x.lower() for x in reviews]
        for review in reviews:
            for keyword in keywords:
                if keyword in review:
                    if keyword in keywordDictionary:
                        keywordDictionary[keyword] += 1
                    else:
                        keywordDictionary.update({keyword : 1})

        sorted_keywords = sorted(keywordDictionary.items())
        print(sorted_keywords)

        # values = list(keywordDictionary.values())
        # keys = list(keywordDictionary.keys()) 
        # maxValue = max(values)
        # make a list of max values
        # maxList = [i for i, j in enumerate(keywordDictionary) if j == maxValue]
        # return keys[values.index(max(values))]
        return sorted_keywords


s = Solution()

# Test Case #0.1
k = 0
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
    "Anacell provides the best services in the city",
    "betacellular has awesome services",
    "Best services provided by anacell, everyone should use anacell",
]
solution = ["anacell", "betacellular"]
output = s.getFrequentKeywords(k, keywords, reviews)
print("%s : output = %s" % (output == solution, output))

# Test Case #0.2
k = 2
keywords = []
reviews = [
    "Anacell provides the best services in the city",
    "betacellular has awesome services",
    "Best services provided by anacell, everyone should use anacell",
]
solution = ["anacell", "betacellular"]
output = s.getFrequentKeywords(k, keywords, reviews)
print("%s : output = %s" % (output == solution, output))

# Test Case #0.3
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = []
solution = ["anacell", "betacellular"]
output = s.getFrequentKeywords(k, keywords, reviews)
print("%s : output = %s" % (output == solution, output))


# Test Case #1
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
    "Anacell provides the best services in the city",
    "betacellular has awesome services",
    "Best services provided by anacell, everyone should use anacell",
]
solution = ["anacell", "betacellular"]
output = s.getFrequentKeywords(k, keywords, reviews)
print("%s : output = %s" % (output == solution, output))
