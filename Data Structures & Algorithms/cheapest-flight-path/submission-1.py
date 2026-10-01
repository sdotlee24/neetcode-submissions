class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for a, b , cost in flights:
            adjList[a].append((b, cost))
        
        # costs[node][s] = cheapest cost to reach `node` using exactly s edges
        costs = [[float('inf')] * (k + 2) for _ in range(n)]
        costs[src][0] = 0
        minHeap = [(0, 0, src)] #cost to get here, stops required, node

        while minHeap:
            c, stops, node = heapq.heappop(minHeap)
            if stops > k or c > costs[node][stops]:
                continue
            for dest, cost in adjList[node]:
                if c + cost < costs[dest][stops+1]:
                    costs[dest][stops+1] = c + cost
                    heapq.heappush(minHeap, (c+cost, stops+1, dest))
        
        best = min(costs[dst])
        return -1 if best == float('inf') else best
