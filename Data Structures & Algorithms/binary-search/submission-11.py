class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binary_search(l, r):
            m = (l + r) // 2
            if l > r:
                return -1
            if nums[m] == target:
                return m
            if nums[m] > target:
                return binary_search(l, m-1)
            else:
                return binary_search(m+1, r)

        
        return binary_search(0, len(nums) - 1)