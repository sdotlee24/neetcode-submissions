class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0
        have = set(coins)
        for i in range(amount+1):
            for c in have:
                if c <= i and dp[i-c] != -1:
                    if dp[i] != -1:
                        dp[i] = min(dp[i],dp[i-c] + 1)
                    else:
                        dp[i] = dp[i-c]+1

        return dp[amount]