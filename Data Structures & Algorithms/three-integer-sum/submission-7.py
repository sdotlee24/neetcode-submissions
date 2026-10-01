class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        prev = float('-inf')
        res = []
        i = 0
        while i < len(nums):
            if nums[i] == prev:
                i += 1
                continue
            
            target = -nums[i]
            prev = nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                comb = nums[l] + nums[r]
                if comb < target:
                    l += 1
                elif comb > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            i += 1
        
        return res

