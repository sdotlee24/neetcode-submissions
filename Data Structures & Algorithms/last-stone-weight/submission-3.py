from _heapq import heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            one, two = heapq.heappop(stones), heapq.heappop(stones)

            rem = one - two
            if rem:
                heapq.heappush(stones, rem)
            
        return 0 if len(stones) == 0 else -stones[0]