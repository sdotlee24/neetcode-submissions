class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur, idx):
            if idx >= len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[idx])
            dfs(cur, idx+1)
            cur.pop()
            dfs(cur, idx+1)

        dfs([], 0)

        return res