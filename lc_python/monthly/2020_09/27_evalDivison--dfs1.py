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
import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        weight = collections.defaultdict(list)
        for idx in range(len(equations)):
            v1 = equations[idx][0]
            v2 = equations[idx][1]
            graph[v1].append(v2)
            weight[v1].append(values[idx])
            graph[v2].append(v1)
            weight[v2].append(1/values[idx])
        def dfs(p, q):
            if p == q: return 1
            for idx, c in enumerate(graph[p]):
                if c not in self.visited:
                    self.visited.append(c)
                    mid_result = dfs(c, q)
                    if mid_result >= 0: return weight[p][idx]*mid_result
            return -1
        results = []
        for v1, v2 in queries:
            if v1 in graph.keys() and v2 in graph.keys():
                self.visited = []
                results.append(max(dfs(v1, v2), -1))
            else:
                results.append(-1)
        return results

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