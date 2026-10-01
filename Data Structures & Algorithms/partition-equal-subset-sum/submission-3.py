class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        target = int(tot/2)

        
        dp = [[False] * (target+1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True
        dp[0][nums[0]] = True
        
        for r in range(1, len(nums)):
            curVal = nums[r]
            for c in range(1, target+1):
                #curVal = r, target = c
                if dp[r-1][c]:
                    dp[r][c] = True
                if c >= curVal and dp[r-1][c-curVal]:
                    dp[r][c] = True
        
        return dp[-1][target]