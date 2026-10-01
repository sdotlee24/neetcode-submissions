class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(cur, idx, count):
            if count == target:
                res.append(cur[:])
                return
            if idx >= len(candidates) or count > target:
                return
            
            cur.append(candidates[idx])
            dfs(cur, idx+1, count + candidates[idx])
            cur.pop()
            idx += 1
            while idx < len(candidates) and candidates[idx] == candidates[idx-1]:
                idx += 1
            dfs(cur, idx, count)


        dfs([], 0, 0)
        return res