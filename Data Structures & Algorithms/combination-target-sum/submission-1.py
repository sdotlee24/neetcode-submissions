class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx, cur, count):
            if count == target:
                res.append(cur[:])
                return
            if idx >= len(nums) or count > target:
                return
            
            cur.append(nums[idx])
            dfs(idx, cur, count + nums[idx])
            cur.pop()
            dfs(idx+1, cur, count)

        dfs(0, [], 0)
        return res