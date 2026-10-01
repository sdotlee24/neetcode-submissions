class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)

        res = nums[0]
        while k != 0:
            res = heapq.heappop(nums)
            k -= 1
        return -res