class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)
        while len(stones) > 1:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)
            remainder = abs(one-two)
            if remainder != 0:
                heapq.heappush(stones, -remainder)
        
        return abs(stones[0]) if stones else 0