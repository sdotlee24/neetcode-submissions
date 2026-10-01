class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)

        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n-1, -1, -1):
            for f in range(i, n):
                if s[i:f+1] in wordDict and dp[f+1]:
                    dp[i] = True
                    break
        
        return dp[0]