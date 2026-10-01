class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # isPalin[i][j] = True if s[i:j+1] is a palindrome
        isPalin = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or isPalin[i+1][j-1]):
                    isPalin[i][j] = True

        res = []
        def dfs(idx, cur):
            if idx == n:
                res.append(cur.copy())
                return
            for i in range(idx, n):
                if isPalin[idx][i]:
                    cur.append(s[idx:i+1])
                    dfs(i + 1, cur)
                    cur.pop()

        dfs(0, [])
        return res