class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, cur):
            if idx == len(nums):
                res.append(cur.copy())
                return
            

            val = nums[idx]
            cur.append(val)
            dfs(idx+1, cur)

            cur.pop()
            while idx < len(nums) and val == nums[idx]:
                idx += 1
            
            dfs(idx, cur)
        
        dfs(0, [])

        return res