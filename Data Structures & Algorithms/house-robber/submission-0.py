class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0, 0] + nums
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i-2], nums[i-1])
        
        return nums[-1]

        #2, 9, 8, 3, 6 => [2, 9, 10, 12, 16]