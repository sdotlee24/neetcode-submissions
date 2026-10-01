class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, temp, total):
            if total == target:
                res.append(temp.copy())
                return
            if total > target:
                return
            
            for idx in range(i, len(nums)):
                    temp.append(nums[idx])
                    dfs(idx, temp, total + nums[idx])
                    temp.pop()
        dfs(0, [], 0)
        return res