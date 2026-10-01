class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]
        for n in nums[1:]:
            newVals = (n, curMax * n, curMin * n)
            curMax = max(newVals)
            curMin = min(newVals)
            res = max(res, curMax)
        return res