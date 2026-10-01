class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def maxProfit(houses):
            if len(houses) <= 2:
                return max(houses)
            houses[1] = max(houses[1], houses[0])
            for i in range(2, len(houses)):
                houses[i] = max(houses[i-1], houses[i-2] + houses[i])
            return houses[-1]
        
        return max(maxProfit(nums[1:]), maxProfit(nums[:-1]))