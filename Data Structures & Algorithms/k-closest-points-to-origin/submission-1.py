class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for x, y in points:
            heapq.heappush(hp, [(x ** 2 + y ** 2), x, y])
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(hp)[1:])

        return res