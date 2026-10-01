class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        nextCandidate = curJump = nums[0]
        res = 1
        i = 0
        while i < len(nums):
            nextCandidate = max(nextCandidate, nums[i]+i)
            if curJump == i and curJump and i != len(nums)-1:
                curJump = nextCandidate
                res += 1
            i += 1

        
        return res
