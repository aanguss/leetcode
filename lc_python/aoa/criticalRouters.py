# https: // leetcode.com/discuss/interview-question/436073/
# You are given an undirected connected graph. An articulation point 
# ( or cut vertex) is defined as a vertex which, when removed along with 
# associated edges, makes the graph disconnected ( or more precisely, 
# increases the number of connected components in the graph). The task is 
# to find all articulation points in the given graph.

# Input:
#   The input to the function/method consists of three arguments:
#       numNodes, an integer representing the number of nodes in the graph.
#       numEdges, an integer representing the number of edges in the graph.
#       edges, the list of pair of integers - A, B representing an edge between the nodes A and B.
# Output:
#   Return a list of integers representing the critical nodes.
# Example:
#   Input: 
#       numNodes = 7, 
#       numEdges = 7, 
#       edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
# Input Node List/Image
#        4
#       / 
#      3
#     / \
#    1   2
#     \ / \
#      0   5
#         /
#        6
# Output: [2, 3, 5]
from typing import List
class Solution:
    def getCriticalRouters(self, numNodes:int, numEdges:int, edges:List[List[int]]) -> List:
        criticalNodes = []

        # create a list of nodes
        nodeList = []
        for edge in edges:
            if edge[0] not in nodeList:
                nodeList.append(edge[0])
            if edge[1] not in nodeList:
                nodeList.append(edge[1])

        # create adjacent list
        adjacentDictionary = {}
        for node in nodeList:
            tempList = []
            for edge in edges:
                if edge[0] == node:
                    tempList.append(edge[1])
                elif edge[1] == node:
                    tempList.append(edge[0])
            adjacentDictionary.update({node:tempList})

        # for i in adjacentDictionary.items():
        #     print(i)

        # go through nodes and remove node id if found anywhere else
        # then perform dfs with stack with new node adj list
        for node in nodeList:
            # print('\nchecking node: %s' % node)
            nodelessAdjDict = adjacentDictionary.copy()
            # print('starting nodelessAdjDict:')
            # for i in nodelessAdjDict.items():
            #     print(i)
            
            if node in nodelessAdjDict:
                del nodelessAdjDict[node]
            for n in nodeList:
                if n == node:
                    continue
                else:
                    if node in nodelessAdjDict: 
                        # print('node in nodelessAdjDict')
                        continue
                    if node in nodelessAdjDict[n]:
                        nodeIndex = nodelessAdjDict[n].index(node)
                        # print(nodelessAdjDict[n])
                        newList = nodelessAdjDict[n].copy()
                        del newList[nodeIndex]
                        # print(newList)
                        nodelessAdjDict.update({n: newList})
            # print('updated nodelessAdjDict:')
            # for i in nodelessAdjDict.items():
            #     print(i)

            nodeVisited = []
            stackList = []
            
            for i,j in nodelessAdjDict.items():
                if j not in nodeVisited:
                    stackList.append(i)
                    break
            
            
            while stackList:
                # print("stackList = %s" % stackList)
                currentNode = stackList.pop()
                # print("currentNode = %s" % currentNode)

                if currentNode not in nodeVisited:
                    nodeVisited.append(currentNode)

                for n in nodelessAdjDict[currentNode]:
                    if n not in nodeVisited:
                        stackList.append(n)

            if len(nodeVisited) < numNodes - 1:
                criticalNodes.append(node)


        # go through edges and remove nodes while tracking if all nodes have been visited
        # for node in nodeList:
        #     print('\nchecking node: %s' % node)
            
        #     # which children are attached to the current node
        #     childrenNodes = []
        #     for edge in edges:
        #         if edge[0] == node:
        #             childrenNodes.append(edge[1])
        #     for edge in edges:
        #         if edge[0] != node and edge[1] in childrenNodes:
        #             childrenNodes.remove(edge[1])
        #     print("children nodes = %s" % childrenNodes)

        #     # which nodes should be counted based on if the current node was gone
        #     nodeVisited = []
        #     for edge in edges:
        #         print("checking edge[0] = %d and edge[1] = %d" % (edge[0], edge[1]))
        #         if edge[0] != node and edge[1] != node and edge[0] not in childrenNodes and edge[1] not in childrenNodes:
        #             if edge[0] not in nodeVisited:
        #                 print("adding edge[0]")
        #                 nodeVisited.append(edge[0])
        #             if edge[1] not in nodeVisited:
        #                 print("adding edge[1]")
        #                 nodeVisited.append(edge[1])
                
        #     print(nodeVisited)
        #     print("len of nodeVisited = %d" % len(nodeVisited))
        #     if len(nodeVisited) < numNodes - 1:
        #         criticalNodes.append(node)

        

        
        return criticalNodes

s = Solution()
numNodes = 7
numEdges = 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
solution = [2, 3, 5]
output = s.getCriticalRouters(numNodes, numEdges, edges)
print("starting edges = %s", edges)
print("%s | output = %s" % (output == solution, output))
