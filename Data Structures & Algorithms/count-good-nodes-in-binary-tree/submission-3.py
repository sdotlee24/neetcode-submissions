# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, high):
            if not node:
                return 0
            highVal = max(node.val, high)
            if node.val >= high:
                return 1 + dfs(node.left, highVal) + dfs(node.right, highVal)
            return dfs(node.left, highVal) + dfs(node.right, highVal)
        
        return dfs(root, root.val)
            
