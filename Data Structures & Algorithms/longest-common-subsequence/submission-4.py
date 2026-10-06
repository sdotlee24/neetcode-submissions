class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        dp = [[0] * (M+1) for _ in range(N+1)]

        for r in range(N):
            for c in range(M):
                if text1[r] == text2[c]:
                    dp[r+1][c+1] = 1 + dp[r][c]
                else:
                    dp[r+1][c+1] = max(dp[r+1][c], dp[r][c+1])

        return dp[N][M]