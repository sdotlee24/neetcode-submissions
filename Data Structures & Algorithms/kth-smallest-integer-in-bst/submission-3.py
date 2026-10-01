# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0, 0]
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res[1] += 1
            if res[1] == k:
                res[0] = node.val
            
            dfs(node.right)

        dfs(root)
        return res[0]