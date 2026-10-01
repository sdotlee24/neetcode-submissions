class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        
        target = int(tot / 2)
        dp = [[False] * (target+1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True
        dp[0][nums[0]] = True

        for r in range(1, len(nums)):
            for c in range(target+1):
                if dp[r-1][c] or nums[r] <= c and dp[r-1][c-nums[r]]:
                    dp[r][c] = True
        return dp[-1][-1]
