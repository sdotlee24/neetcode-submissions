class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        
        res = 0
        for n in nums:
            if n-1 not in seen:
                cur = n
                temp = 0
                while cur in seen:
                    temp += 1
                    cur += 1
                res = max(res, temp)
        return res