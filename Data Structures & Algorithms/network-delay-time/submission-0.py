class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, t in times:
            graph[a].append((b, t))
        dist = {node: float('inf') for node in range(1, n+1)}
        dist[k] = 0

        minHeap = [(0, k)]

        while minHeap:
            t, node = heapq.heappop(minHeap)
            if t > dist[node]:
                continue
            for neighbour, dur in graph[node]:
                if t + dur < dist[neighbour]:
                    dist[neighbour] = t + dur
                    heapq.heappush(minHeap, (t+dur, neighbour))
        
        ans = max(dist.values())
        return ans if ans != float('inf') else -1
