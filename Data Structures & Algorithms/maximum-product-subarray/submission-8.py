class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = curMax = nums[0]
        res = curMin
        for n in nums[1:]:
            newVals = (n, curMax * n, curMin * n)
            curMin = min(newVals)
            curMax = max(newVals)
            res = max(res, curMax)
        
        return res
