class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        for n in nums:
            if n-1 not in seen:
                counter = 0
                x = n
                while x in seen:
                    x += 1
                    counter += 1
                longest = max(longest, counter)
        
        return longest