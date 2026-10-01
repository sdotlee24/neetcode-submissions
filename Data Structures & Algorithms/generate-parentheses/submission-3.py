class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, stck, op, cl):
            if len(cur) == 2 * n and len(stck) == 0:
                res.append(cur)
                return
            
            if len(stck) != 0 and cl < n:
                temp = stck.pop()
                dfs(cur + ')', stck, op, cl+1)
                stck.append(temp)
            if op < n:
                stck.append('(')
                dfs(cur + '(', stck, op+1, cl)
                stck.pop()
        dfs('', [], 0, 0)
        return res
