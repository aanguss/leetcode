from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getVal(self):
        return self.val

class Solution:
    _dfsqueue = []

    def DFS(self, root: TreeNode):
        if root.left:
            self.DFS(root.left)
        if root.right:
            self.DFS(root.right)
        self._dfsqueue.append(root)

    def printDFS(self, root: TreeNode):
        self.DFS(root)

        # for s in self._queue:
        while self._dfsqueue:
            s = self._dfsqueue.pop(0)
            print(s.val, end = ' ')
        print('\r')
    
    def printBFS(self, root: TreeNode):
        visited = []
        if root:
            visited.append(root)
            print(root.val, end = ' ')
        current = root
        while current:
            if current.left:
                visited.append(current.left)
                print(current.left.val, end = ' ')
            if current.right:
                visited.append(current.right)
                print(current.right.val, end = ' ')
        
            visited.pop(0)
            if not visited:
                break
            current = visited[0]
        print('\r')

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        zigzagList = []
        visited = []
        level = 0
        
        if root:
            zigzagList.append([])
            visited.append(root)
            visited.append(None)
            while visited:
                current = visited.pop(0)
                
                if current:
                    zigzagList[level].append(current.val)
                    if current.left:
                        visited.append(current.left)
                    if current.right:
                        visited.append(current.right)
                else:
                    if visited:
                        visited.append(None)
                        zigzagList.append([])
                        level += 1
            print(zigzagList)

            # currently setup as BFS but lets just reverse every other?
            leftLevel = True
            
            for i in range(0, level + 1):
                if not leftLevel:
                    zigzagList[i].reverse()
                leftLevel = not leftLevel
                    
            print(zigzagList)
        
        return zigzagList

    def printBinaryTree(self, root: TreeNode):
        print(root.val, end = ' ')
        if root.left:
            self.printBinaryTree(root.left)
        if root.right:
            self.printBinaryTree(root.right)
        

t1 = TreeNode(val = 3)
t1.left = TreeNode(val = 9)
# t1.left.left = TreeNode(val = 6)
# t1.left.right = TreeNode(val = 10)
t1.right = TreeNode(val = 20)
t1.right.left = TreeNode(val = 15)
t1.right.right = TreeNode(val = 7)

s = Solution()
print("PBT: ", end = '')
s.printBinaryTree(t1)
print('\r')
print("BFS: ", end = '')
s.printBFS(t1)
print("DFS: ", end = '')
s.printDFS(t1)
print("ZIG: ", end = '')
s.zigzagLevelOrder(t1)
print('\r')
# t1 = TreeNode(val=10)
# t1.val = 1

# print(t1.getVal())

