# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [0, True]
            

            left, v = dfs(node.left)
            right, v1 = dfs(node.right)
            if abs(right-left) > 1 or not v or not v1:
                v = False
            
            return [max(left, right) + 1, v]
        
        return dfs(root)[1]