class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(visited, cur):
            if len(visited) == len(nums):
                res.append(cur[:])
                return
            for i in nums:
                if i not in visited:
                    visited.add(i)
                    cur.append(i)
                    dfs(visited, cur)
                    visited.remove(i)
                    cur.pop()

        dfs(set(), [])
        return res