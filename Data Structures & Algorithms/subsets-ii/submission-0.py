class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort(key=lambda x: x)
        def dfs(cur, idx):
            if idx == len(nums):
                res.append(cur[:])
                return
            
            cur.append(nums[idx])
            dfs(cur, idx+1) #normal dfs
            cur.pop()
            idx += 1
            while idx < len(nums) and nums[idx] == nums[idx-1]:
                idx += 1
            dfs(cur, idx)

        dfs([], 0)
        return res