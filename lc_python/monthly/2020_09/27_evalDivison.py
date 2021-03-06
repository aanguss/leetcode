# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3474/
# https://leetcode.com/problems/evaluate-division/
#
# You are given equations in the format A / B = k, where A and B are variables 
# represented as strings, and k is a real number (floating-point number). 
# Given some queries, return the answers. If the answer does not exist, 
# return -1.0.
#
# The input is always valid. You may assume that evaluating the queries will 
# result in no division by zero and there is no contradiction.
#
# Example 1:
#     Input: 
#         equations = [["a","b"],["b","c"]], 
#         values = [2.0,3.0], 
#         queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
#     Output: 
#         [6.00000,0.50000,-1.00000,1.00000,-1.00000]
#     Explanation: 
#         Given: a / b = 2.0, b / c = 3.0 ---- a / b = 2, b / a = 1/2
#         queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
#         return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
#
# Example 2:
#     Input: 
#         equations = [["a","b"],["b","c"],["bc","cd"]], 
#         values = [1.5,2.5,5.0], 
#         queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
#     Output: 
#         [3.75000,0.40000,5.00000,0.20000]
#
# Example 3:
#     Input: 
#         equations = [["a","b"]], 
#         values = [0.5], 
#         queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
#     Output: 
#         [0.50000,2.00000,-1.00000,-1.00000]
#
# Constraints:
#     1 <= equations.length <= 20
#     equations[i].length == 2
#     1 <= equations[i][0], equations[i][1] <= 5
#     values.length == equations.length
#     0.0 < values[i] <= 20.0
#     1 <= queries.length <= 20
#     queries[i].length == 2
#     1 <= queries[i][0], queries[i][1] <= 5
#     equations[i][0], equations[i][1], queries[i][0], queries[i][1] 
#         consist of lower case English letters and digits.
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        debug = False
        solutionList = []
        variables = {}
        if debug: print(equations)
        for i in range(len(equations)):
            if debug: print(equations[i])
            if equations[i][0] + '/' + equations[i][1] not in variables:
                variables[equations[i][0] + '/' + equations[i][1]] = values[i]
            if equations[i][1] + '/' + equations[i][0] not in variables:
                variables[equations[i][1] + '/' + equations[i][0]] = 1/values[i]
        
        nothingAdded = False
        while nothingAdded == False:
            extraVariables = {}
            nothingAdded = True
            for key, variable in variables.items():
                if debug: print("%s: %s" % (key, variable))
                divIndex1 = key.find('/')
                numerator1 = key[divIndex1 + 1:]
                denominator1 = key[:divIndex1]

                for k, v in variables.items():
                    divIndex2 = k.find('/')
                    numerator2 = k[divIndex2 + 1:]
                    denominator2 = k[:divIndex2]
                    if numerator2 == denominator1:
                        if numerator1 + '/' + denominator2 not in extraVariables:
                            extraVariables[numerator1 + '/' + denominator2] = 1 / (variable * v)
                        if denominator2 + '/' + numerator1 not in extraVariables:
                            extraVariables[denominator2 + '/' + numerator1] = (variable * v)
                    if numerator1 == denominator2:
                        if numerator2 + '/' + denominator1 not in extraVariables:
                            extraVariables[numerator2 + '/' + denominator1] = 1 / (variable * v)
                        if denominator1 + '/' + numerator2 not in extraVariables:
                            extraVariables[denominator1 + '/' + numerator2] = (variable * v)
            if debug: print("variables =", variables)
            if debug: print("extras =", extraVariables)
            for key in extraVariables:
                if key not in variables:
                    nothingAdded = False
                    variables[key] = extraVariables[key]

        for query in queries:
            queryKey = query[0] + '/' + query[1]
            if queryKey not in variables:
                solutionList.append(-1)
            else:
                solutionList.append(variables[queryKey])
        if debug: print('final variables =', variables)
        return solutionList

s = Solution()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
solution = [6.00000,0.50000,-1.00000,1.00000,-1.00000]
output = s.calcEquation(equations, values, queries)
print("%s | %s" % ('PASS' if output == solution else 'FAIL', output))

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
solution = [3.75000,0.40000,5.00000,0.20000]
output = s.calcEquation(equations, values, queries)
print("%s | %s" % ('PASS' if output == solution else 'FAIL', output))

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
solution = [0.50000,2.00000,-1.00000,-1.00000]
output = s.calcEquation(equations, values, queries)
print("%s | %s" % ('PASS' if output == solution else 'FAIL', output))

equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
solution = [360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000]
output = s.calcEquation(equations, values, queries)
print("%s | %s" % ('PASS' if output == solution else 'FAIL', output))