class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = 0
        adjList = defaultdict(list)
        for i in range(len(points)):
            points[i] = tuple(points[i])
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a, b = points[i], points[j]
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                adjList[a].append((dist, b))
                adjList[b].append((dist, a))
        
        visited = set()
        minHeap = [(0, points[0])]
        N = len(points)
        while len(visited) < N:
            dist, key = heapq.heappop(minHeap)
            if key in visited:
                continue
            visited.add(key)
            cost += dist
            for child in adjList[key]:
                heapq.heappush(minHeap, child)
        
        return cost