class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 5 5 4 3 2 1 1, k = 3
        return heapq.nlargest(k, nums)[-1]