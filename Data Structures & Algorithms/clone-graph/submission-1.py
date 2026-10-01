"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}
        def dfs(n):
            if n in nodeMap:
                return nodeMap[n]
            cpy = Node(n.val)
            nodeMap[n] = cpy
            for child in n.neighbors:
                cpy.neighbors.append(dfs(child))
            return cpy
        
        return dfs(node) if node else None