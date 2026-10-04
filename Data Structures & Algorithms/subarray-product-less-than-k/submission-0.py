class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #[10, 5, 2, 6] -> 10, [10, 5],
        res = 0
        tot = 1
        l = 0
        for r in range(len(nums)):
            tot *= nums[r]
            while l <= r and tot >= k:
                tot //= nums[l]
                l += 1
            res += (r-l+1)
        return res
            