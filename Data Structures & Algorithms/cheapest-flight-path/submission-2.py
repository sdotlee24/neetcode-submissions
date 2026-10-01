class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for a, b , cost in flights:
            adjList[a].append((b, cost))
        
        costs = [[float('inf')] * (k + 2) for _ in range(n)]
        #costs[node][cost]

        costs[src][0] = 0
        minHeap = [(0, 0, src)] #(price, stops, node)

        while minHeap:
            p, s, n = heapq.heappop(minHeap)
            if s > k or costs[n][s] < p:
                continue

            for node, price in adjList[n]:
                if p + price < costs[node][s+1]:
                    costs[node][s+1] = p + price
                    heapq.heappush(minHeap, (p+price, s+1, node))
        
        res = min(costs[dst])
        return res if res != float('inf') else -1