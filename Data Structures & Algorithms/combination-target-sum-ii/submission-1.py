class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        #1 2 2 4 5 6 9

        def dfs(idx, arr, total):
            if total == target:
                res.append(arr.copy())
                return
            if total > target:
                return
            prev = 0
            for i in range(idx, len(candidates)):
                if prev != candidates[i]:
                    arr.append(candidates[i])
                    dfs(i+1, arr, total + candidates[i])
                    arr.pop()
                prev = candidates[i]
            
        dfs(0, [], 0)
        return res