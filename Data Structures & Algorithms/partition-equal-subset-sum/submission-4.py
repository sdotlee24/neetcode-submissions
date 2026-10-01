class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        
        target = tot / 2
        memo = {}

        def traverse(i, subtotal):
            if subtotal == target:
                return True
            if i == len(nums):
                return False
            if (i, subtotal) in memo:
                return memo[(i, subtotal)]
            
            works = traverse(i+1, subtotal) or traverse(i+1, subtotal+nums[i])
            memo[(i, subtotal)] = works

            return works
        
        return traverse(0, 0)
