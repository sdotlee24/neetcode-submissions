class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        # [48, 24, 12, 8]
        temp = [1] * len(nums)
        for i in range(1, len(nums)):
            temp[i] = temp[i-1] *nums[i-1]
        
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            temp[i] *= (prev)
            prev *= nums[i]
        return temp