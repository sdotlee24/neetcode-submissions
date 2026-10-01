class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        idxMap = {}
        for i in range(len(inorder)):
            idxMap[inorder[i]] = i

        pre_idx = 0

        def dfs(lb, rb):
            nonlocal pre_idx

            if lb > rb:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1

            node = TreeNode(root_val)

            splitIdx = idxMap[root_val]

            node.left = dfs(lb, splitIdx - 1)
            node.right = dfs(splitIdx + 1, rb)

            return node

        return dfs(0, len(inorder) - 1)