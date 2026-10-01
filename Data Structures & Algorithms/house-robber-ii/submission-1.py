class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def maxProfit(houses):
            prev, curr = 0, 0
            for x in houses:
                prev, curr = curr, max(curr, prev + x)
            return curr

        return max(maxProfit(nums[1:]), maxProfit(nums[:-1]))