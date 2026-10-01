class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        curJump = nums[i]
        if len(nums) == 1:
            return True
        while curJump and i < len(nums):
            curJump -= 1

            curJump = max(curJump, nums[i])
            i += 1

        return True if i == len(nums) else False
