class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo = set()
        for n in nums:
            if n in memo:
                return True
            memo.add(n)
        return False