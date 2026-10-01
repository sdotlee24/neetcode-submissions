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
                return True, 0
            
            balLeft, hLeft = dfs(node.left)
            balRight, hRight = dfs(node.right)
        
            if not balLeft or not balRight:
                return False, hLeft
            
            if abs(hLeft - hRight) > 1:
                return False, hLeft
            
            return True, max(hLeft, hRight) + 1
        
        return dfs(root)[0]