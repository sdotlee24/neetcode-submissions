class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = min(nums) - 1
        temp = res
        for n in nums:
            if temp + n < n:
                temp = n
            else:
                temp += n
            print(temp)
            res = max(res, temp)
        return res