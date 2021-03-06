# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3519/
# https://leetcode.com/problems/minimum-height-trees/
#
# Minimum Height Trees
# A tree is an undirected graph in which any two vertices are connected by 
# exactly one path. In other words, any connected graph without simple cycles 
# is a tree.
#
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 
# edges where edges[i] = [ai, bi] indicates that there is an undirected edge 
# between the two nodes ai and bi in the tree, you can choose any node of the 
# tree as the root. When you select a node x as the root, the result tree has 
# height h. Among all possible rooted trees, those with minimum height 
# (i.e. min(h))  are called minimum height trees (MHTs).
#
# Return a list of all MHTs' root labels. You can return the answer in any order.
#
# The height of a rooted tree is the number of edges on the longest downward 
# path between the root and a leaf.
#
# Example 1:
#     Input: n = 4, edges = [[1,0],[1,2],[1,3]]
#     Output: [1]
#     Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
# Example 2:
#     Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
#     Output: [3,4]
# Example 3:
#     Input: n = 1, edges = []
#     Output: [0]
# Example 4:
#     Input: n = 2, edges = [[0,1]]
#     Output: [0,1]
# Constraints:
#     1 <= n <= 2 * 104
#     edges.length == n - 1
#     0 <= ai, bi < n
#     ai != bi
#     All the pairs (ai, bi) are distinct.
#     The given input is guaranteed to be a tree and there will be no repeated edges.
#
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == None or edges == None or len(edges) == 0:
            return [0]
        debug = False
        nDict = {}
        rootList = []

        for i in range(n):
            nDict[i] = []
        # if debug: 
        #     for i in nDict: print(i, nDict[i])
        for e in edges:
            nDict[e[0]].append(e[1])
            nDict[e[1]].append(e[0])
            # if e[0] < e[1]:
            #     nDict[e[0]].append(e[1])
            # else:
            #     nDict[e[1]].append(e[0])
        if debug: 
            for i in nDict: print(i, nDict[i])

        for i in range(n):
            iCount = 0
            rootVal = None
            for k in nDict:
                if i in nDict[k]:
                    # if debug: print("%d in [%d] = %s" % (i, k, nDict[k]))
                    iCount += 1
                    rootVal = k
            if iCount == 1:
                # if debug: print("found 1 for %d" % rootVal)
                if rootVal not in rootList:
                    rootList.append(rootVal)
        rootList.sort()

        queueList = []
        for k in nDict:
            if debug: print(nDict[k])
            if len(nDict[k]) == 1:
                queueList.append(k)

        # couldnt figure this part out until looked at solution
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(queueList)
            tempQueue = []
            
            while queueList:
                current = queueList.pop()
                if debug: print("current=",current)
                for i in nDict[current]:
                    if debug: print("i=", i)
                    if debug: print("nDict[i]=", nDict[i])
                    nDict[i].remove(current)
                    if debug: print("nDict[i]=", nDict[i])
                    if len(nDict[i]) == 1:
                        tempQueue.append(i)
            queueList = tempQueue
        
        if debug: 
            for i in nDict: print(i, nDict[i])

        queueList.sort()
        return queueList


s = Solution()
n = 4
edges = [[1,0],[1,2],[1,3]]
solution = [1]
output = s.findMinHeightTrees(n, edges)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
solution = [3,4]
output = s.findMinHeightTrees(n, edges)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

n = 1
edges = []
solution = [0]
output = s.findMinHeightTrees(n, edges)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

n = 2
edges = [[0,1]]
solution = [0,1]
output = s.findMinHeightTrees(n, edges)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

n = 6
edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
solution = [3]
output = s.findMinHeightTrees(n, edges)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))


# neighbors = [set() for i in range(n)]
# print(neighbors)
# for start, end in edges:
#     neighbors[start].add(end)
#     neighbors[end].add(start)
# print("neighbors=",neighbors)

#  # Initialize the first layer of leaves
# leaves = []
# for i in range(n):
#     if len(neighbors[i]) == 1:
#         leaves.append(i)
# print("leaves=",leaves)

# # Trim the leaves until reaching the centroids
# remaining_nodes = n
# while remaining_nodes > 2:
#     remaining_nodes -= len(leaves)
#     new_leaves = []
#     # remove the current leaves along with the edges
#     print("leaves=",leaves)
#     while leaves:
#         leaf = leaves.pop()
#         print("leaf=",leaf)
#         print("neighbors[leaf]=",neighbors[leaf])
#         for neighbor in neighbors[leaf]:
#             print("neighbor=",neighbor)
#             neighbors[neighbor].remove(leaf)
#             print("---neighbors=",neighbors)
#             if len(neighbors[neighbor]) == 1:
#                 print("-----added neighbor=",neighbor)
#                 new_leaves.append(neighbor)
#     # prepare for the next round
#     leaves = new_leaves

# # The remaining nodes are the centroids of the graph
# print(leaves)