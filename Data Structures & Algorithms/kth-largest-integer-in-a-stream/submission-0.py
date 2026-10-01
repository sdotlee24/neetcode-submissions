class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k
        heapq.heapify(self.arr)

    def add(self, val: int) -> int:
        #[1, 2, 3, 4, 5], k = 2
        heapq.heappush(self.arr, val)
        while len(self.arr) > self.k:
            heapq.heappop(self.arr)
        return self.arr[0]
