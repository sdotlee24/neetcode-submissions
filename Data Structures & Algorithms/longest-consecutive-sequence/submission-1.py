class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set(nums)
        for n in nums:
            if n-1 in seen:
                continue
            t = n
            temp = 0
            while t in seen:
                temp += 1
                t += 1
            res = max(res, temp)
        
        return res