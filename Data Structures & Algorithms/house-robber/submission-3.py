class Solution:
    def rob(self, nums: List[int]) -> int:
        i, j = 0, 0
        for n in nums:
            newI = i + n
            i = j
            j = max(newI, j)
        return j
        
        
        