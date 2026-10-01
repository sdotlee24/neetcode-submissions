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
        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]

            cpy = Node(node.val)
            nodeMap[node] = cpy
            for nb in node.neighbors:
                cpy.neighbors.append(dfs(nb))
            
            return cpy
        
        return dfs(node) if node else None