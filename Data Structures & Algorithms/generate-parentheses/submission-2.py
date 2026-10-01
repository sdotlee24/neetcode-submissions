class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(op, cl, temp):
            if len(temp) == n * 2:
                res.append(temp)
                return
            
            if op < n:
                dfs(op + 1, cl, temp + '(')
            
            if op > cl:
                dfs(op, cl + 1, temp + ')')
        dfs(0, 0, "")
        return res
