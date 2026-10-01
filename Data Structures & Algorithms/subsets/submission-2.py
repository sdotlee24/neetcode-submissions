class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, cur):
            if i == len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.remove(nums[i])
            dfs(i+1, cur)

        dfs(0, [])
        return res
