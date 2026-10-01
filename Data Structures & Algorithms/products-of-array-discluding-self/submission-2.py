class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    # [1, 2, 4, 6]
    #  1  1  2  8
    #  48 24 6  1   
        acc = [1] * len(nums)
        for i in range(1, len(nums)):
            acc[i] = acc[i-1] * nums[i-1]
        
        prev = 1
        for j in range(len(nums)-2, -1, -1):
            acc[j] *= prev * nums[j+1]
            prev = nums[j+1] * prev
        return acc