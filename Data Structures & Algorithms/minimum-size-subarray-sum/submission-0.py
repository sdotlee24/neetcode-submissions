class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        accum = 0
        l = 0
        for r in range(len(nums)):
            accum += nums[r]
            while accum >= target:
                res = min(res, r-l+1)
                accum -= nums[l]
                l += 1

        return res if res != len(nums) + 1 else 0