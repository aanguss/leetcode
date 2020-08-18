# https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/894/
##
# Given a 2d grid map of '1's (land) and '0's (water), 
# count the number of islands. An island is surrounded by water 
# and is formed by connecting adjacent lands horizontally or 
# vertically. You may assume all four edges of the grid are all 
# surrounded by water.
##
# Example 1
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
##
# Example 2
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 # no islands since grid is empty
        islandLists = [[]]
        islandGraph = {}
        islandsIndex = 0
        # onIsland = True
        for row in range(0,len(grid)):
            for col in range(0,len(grid[0])):
                print(grid[row][col], end = '  ')
                if (grid[row][col] == '1'):
                    location = len(grid[0]) * row + col
                    islandLists[islandsIndex].append(location)
                    # check adjacent locations
                    islandGraph[location] = self.getAdjacentNodes(grid, row, col)
            print("\r")

        # print("island locations: ", end = '')
        # for x in islandLists:
        #     for y in x:
        #         print(y, end = ' ')
        # print('\n')

        print("island graphs: ", end = '')
        print(islandGraph)
        # for x in islandGraph:
        #     for y in x:
        #         print(y, end = ' ')
        print('\r')

        islandEdges = self.getIslandEdges(islandGraph)
        print("island edges: ", end = '')
        print(islandEdges)
        print('\r')

        islandsIsolated = self.getIslandsIsolated(islandGraph)
        print("islands isolated: ", end = '')
        print(islandsIsolated)
        print('\r')

        maxRows = len(grid)
        maxCols = len(grid[0])
        islandGroups = self.getIslandGroups(maxRows, maxCols, islandEdges, islandsIsolated)
        print("island groups: ", end = '')
        # for group in islandGroups:
            # print(group)
        print(islandGroups)
        print('\r')

        islandLeaderList = self.setIslandRoots(islandGroups)
        print("island leader list: ", end = '')
        print(islandLeaderList)
        print('\r')

        islandLeaders = self.getIslandLeaders(islandLeaderList)
        print("island leaders: ", end = '')
        print(islandLeaders)
        print('\r')

        return len(islandLeaders) + len(islandsIsolated)

    def getAdjacentNodes(self, grid: List[List[str]], row: int, col: int) -> List[int]:
        adjList = []
        testLocations = [[row-1,col],[row+1,col],[row,col-1],[row,col+1]]
        # print(f"Testing row = {row} and col = {col}")
        for loc in testLocations:
            # print(f"loc0 = {loc[0]} loc1 = {loc[1]}")
            location = len(grid[0]) * loc[0] + loc[1]
            if (loc[0] >= 0 and loc[0] < len(grid) and loc[1] >= 0 and loc[1] < len(grid[0])):
                if (grid[loc[0]][loc[1]] == '1'):
                    adjList.append(location)
        return adjList

    def getIslandEdges(self, nodes):
        edgeList = []
        for node in nodes:
            # print(node)
            # if nodes[node] == '':
            #     edgeList.append(node)
            for n in nodes[node]:
                # print(f"{node},{n}")
                # edgeList.append(f"{node},{n}")
                if (node < n):
                    if [node,n] not in edgeList:
                        edgeList.append([node,n])
                else:
                    if [n,node] not in edgeList:
                        edgeList.append([n,node])
        return edgeList
    
    def getIslandsIsolated(self, nodes):
        isolatedList = []
        for node in nodes:
            # print(node)
            if not nodes[node]:
                # print("empty found")
                isolatedList.append(node)
        return isolatedList

    def getIslandGroups(self, rows, cols, edges, isolated):
        # groups = [[]]
        # groupIndex = 0
        
        # for edgeIndex in range(len(edges) - 1, -1, -1):
        #     for edgeTest in edges[edgeIndex]:
        #         print(edgeTest)
        #         for edgeList in range(0, edgeIndex):
        #             print(f"edges[edgeindex] = {edges[edgeIndex]} and edges[edgeList] = {edges[edgeList]}")
        #             for edge in edges[edgeList]:
        #                 print(edge)
        #                 if (edgeTest == edge):
        #                     print("match")
        #                     notInGroup = True
        #                     for group in groups:
        #                         if edges[edgeIndex] in group:
        #                             notInGroup = False
        #                     if (notInGroup == True):
        #                         groups.append(edges[edgeIndex])
        #                     elif (notInGroup == False):
        #                         for groupIndex in range(len(groups)):
        #                             if edges[edgeIndex] in groups[groupIndex]:
        #                                 groups[groupIndex].append(edges[edgeIndex])
                
        #     print('\r')
        # islandMap = [[]]
        islands = [-1 for x in range(rows * cols)]
        # print(islands)
        # islandMap = [[-1 for x in range(cols)] for y in range(rows)]
        for edge in edges:
            if islands[edge[0]] == -1 and islands[edge[1]] == -1:
                if (edge[0] < edge[1]):
                    islands[edge[1]] = edge[0]
                else:
                    islands[edge[0]] = edge[1]
            elif islands[edge[0]] != -1 and islands[edge[1]] == -1:
                islands[edge[1]] = edge[0]
            elif islands[edge[1]] != -1 and islands[edge[0]] == -1:
                islands[edge[0]] = edge[1]
                


        #     print(edge, end=' = ')
        #     vertices = self.getRowCol(rows,cols,edge)
        #     for vertex in vertices:
        #     # print(self.getRowCol(rows,cols,edge))
        #         print(vertex, end=' ')
        #     print('\r')
        #     # print(self.getRowCol(rows,cols,edge[1]))
        # # for row in range(0, rows):
        # #     for col in range(0, cols):
        # #         islandMap[row][col] = -1
        # # first = True
        # # for edge in edges:
        # #     print(f"edge[0] = {edge[0]}, edge[1] = {edge[1]}")
        # #     if first:
        # #         islandMap[edge[0]][edge[1]] = 1
        # #         first = False
        # #     else:
        # #         print(edge)
        # #         for vertexOne in edge:
        # #             print(vertexOne)
        # #     print('\r')

        return islands

    def getRowCol(self, rows, cols, pos):
        row1 = pos[0] % rows
        col1 = pos[0] % cols

        row2 = pos[1] % rows
        col2 = pos[1] % cols

        return [[row1,col1],[row2,col2]]

    def setIslandRoots(self, groups):
        for i in range(len(groups)):
            if groups[i] > 0:
                groups[i] = self.findRoot(groups, i)
        return groups

    def findRoot(self, group, i):
        if (group[i] < 0):
            return i
        else:
            rootIndex = self.findRoot(group, group[i])
            # group[i] = rootIndex
            return rootIndex
    
    def getIslandLeaders(self, islandLeaders):
        leaderList = []
        for leader in islandLeaders:
            if leader != -1:
                if leader not in leaderList:
                    leaderList.append(leader)
        return leaderList
        

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
] # should return 1

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
] # should return 3

grid3 = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]] # should return 1

s = Solution()

islands = s.numIslands(grid1)
print(f"Number of islands on grid1 = {islands}")

islands = s.numIslands(grid2)
print(f"Number of islands on grid2 = {islands}")

islands = s.numIslands(grid3)
print(f"Number of islands on grid3 = {islands}")