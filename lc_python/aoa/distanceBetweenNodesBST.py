# https: // leetcode.com/discuss/interview-question/376375/
#
# Given a list of unique integers nums, construct a BST from it(you need to insert 
# nodes one-by-one with the given order to get the BST) and find the distance 
# between two nodes node1 and node2. Distance is the number of edges between two 
# nodes. If any of the given nodes does not appear in the BST, return -1.
#
# Example 1:
#     Input: nums = [2, 1, 3], node1 = 1, node2 = 3
#     Output: 2
#     Explanation:
#         2
#       /   \
#      1     3
from typing import List  

# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def findNode(self, node, value):
        # Base Cases: node is null or value is present at node
        if node is None or node.val == value:
            return node
        # value is greater than node's value
        if node.val < value:
            return self.findNode(node.right, value)
        else:
            # value is smaller than node's value
            return self.findNode(node.left, value)
    def insertNode(self, node, value):
        if node is None:
            return TreeNode(value)
        else:
            if node.val == value:
                return node
            elif node.val < value:
                node.right = self.insertNode(node.right, value)
            else:
                node.left = self.insertNode(node.left, value)
        return node
    def printTree(self, node):
        if node:
            self.printTree(node.left)
            print(node.val)
            self.printTree(node.right)

class Solution:
    def distanceFromNode(self, node, value):
        if node.val == value:
            return 0
        elif node.val > value:
            return 1 + self.distanceFromNode(node.left, value)
        return 1 + self.distanceFromNode(node.right, value)

    def findCommonParent(self, node, value1, value2):
        currentNode = node
        while currentNode:
            commonParent = currentNode.val
            if value1 > commonParent and value2 > commonParent:
                currentNode = currentNode.right
            elif value1 < commonParent and value2 < commonParent:
                currentNode = currentNode.left
            else:
                return currentNode
                
    def getDistanceBetweenNodes(self, nums: List[int], node1: int, node2: int) -> int:
        
        print("nums = %s" % nums)

        # create tree
        tree = TreeNode(nums[0])
        for i in range(len(nums)):
            tree.insertNode(tree, nums[i])
        # tree.printTree(tree)
        
        # dfs stack - https://www.geeksforgeeks.org/iterative-depth-first-traversal/
        # stackList.append(tree)
        # while stackList:
        #     currentNode = stackList.pop()
        #     entirePath.append(currentNode.val)
        #     # print("currentNode.val = %s" % currentNode.val)
            
        #     if currentNode.val == node1:
        #         # print("found node1")
        #         node1_path = entirePath.copy()
        #         print(node1_path)
        #     elif currentNode.val == node2:
        #         # print("found node2")
        #         node2_path = entirePath.copy()
        #         print(node2_path)
                
        #     if currentNode not in visitedNodes:
        #         visitedNodes.append(currentNode)

        #     if currentNode.left and currentNode.left not in visitedNodes:
        #         # print("found left")
        #         stackList.append(currentNode.left)
        #     if currentNode.right and currentNode.right not in visitedNodes:
        #         # print("found right")
        #         stackList.append(currentNode.right)

        # if len(node1_path) == 0:
        #     return -1
        # elif len(node2_path) == 0:
        #     return -1

        # distance1 = 0
        # for i in node1_path:
        #     if node1_path[0] >= node1:
        #         if i < node1_path[0] and i > node1:
        #             distance1 += 1
        #     elif node1_path[0] < node1:
        #         if i > node1_path[0] and i < node1:
        #             distance1 +=1

        # distance2 = 0
        # for i in node2_path:
        #     if node2_path[0] >= node2:
        #         if i < node2_path[0] and i > node2:
        #             distance2 += 1
        #     elif node2_path[0] < node2:
        #         if i > node2_path[0] and i < node2:
        #             distance2 += 1

        # distance = abs(distance2 - distance1) + 1  # add 1 for the parent

        parentNode = self.findCommonParent(tree, node1, node2)
        print("parentNode = %d" % parentNode.val)
        distance1 = self.distanceFromNode(parentNode, node1)
        distance2 = self.distanceFromNode(parentNode, node2)
        distance = distance1 + distance2
        
        return distance

    

s = Solution()
# nums = [2, 1, 3]
# node1 = 1
# node2 = 3
# solution = 2
# output = s.getDistanceBetweenNodes(nums, node1, node2)
# print("\n%s | %s\n" % (output == solution, output))

nums = [50, 30, 20, 40, 70, 60, 80]
node1 = 20
node2 = 40
solution = 2
output = s.getDistanceBetweenNodes(nums, node1, node2)
print("%s | %s\n" % (output == solution, output))

nums = [50, 30, 20, 40, 70, 60, 80]
node1 = 20
node2 = 70
solution = 3
output = s.getDistanceBetweenNodes(nums, node1, node2)
print("%s | %s\n" % (output == solution, output))




# r = TreeNode(50)
# r.insertNode(r, 30)
# r.insertNode(r, 20)
# r.insertNode(r, 40)
# r.insertNode(r, 70)
# r.insertNode(r, 60)
# r.insertNode(r, 80)
# r.printTree(r)
# print("%s is %s from root" % (node1, s.distanceFromRoot(r, node1)))
# print("%s is %s from root" % (node2, s.distanceFromRoot(r, node2)))
