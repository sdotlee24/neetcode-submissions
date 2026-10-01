class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(cur, curMap):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in nums:
                if i not in curMap:
                    curMap.add(i)
                    cur.append(i)
                    dfs(cur, curMap)
                    cur.pop()
                    curMap.remove(i)
        
        dfs([], set())
        return res