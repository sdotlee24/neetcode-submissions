class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        checkbook = {(r, c): float('inf') for r in range(len(grid)) for c in range(len(grid[0]))}
        checkbook[(0, 0)] = grid[0][0]

        DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if time > checkbook[(r, c)]:
                continue
            
            for dr, dc in DIR:
                newR, newC = dr+r, dc+c
                if (0 <= newR < len(grid) and 0 <= newC < len(grid[0])):
                    newTime = max(time, grid[newR][newC])
                    if newTime < checkbook[(newR, newC)]:
                        heapq.heappush(minHeap, (newTime, newR, newC))
                        checkbook[(newR, newC)] = newTime
                    
        return int(checkbook[(len(grid)-1, len(grid[0])-1)])
