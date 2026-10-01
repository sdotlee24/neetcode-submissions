# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)

            res[0] = max(res[0], left + node.val, right + node.val, node.val, left + right + node.val)
            maxSubPath = max(left+node.val, right+node.val, node.val, 0)

            return maxSubPath
        dfs(root)
        return res[0]