class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0


        for i in range(1, amount+1):
            for c in coins:
                if c == i:
                    dp[i] = 1
                    break
                if c < i and dp[i-c] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i-c]+1
                    else:
                        dp[i] = min(dp[i-c]+1, dp[i])

        return dp[-1]