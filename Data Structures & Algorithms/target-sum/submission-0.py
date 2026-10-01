class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # (curSum, i)

        def traverse(i, curSum):
            if i == len(nums):
                return 1 if curSum == target else 0
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            
            res = traverse(i+1, curSum-nums[i]) + traverse(i+1, curSum+nums[i])
            memo[(i,curSum)] = res

            return res

        return traverse(0,0)