class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))

        dists = {node: float('inf') for node in range(1, n + 1)}
        dists[k] = 0
        heap = [(0, k)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dists[node]:
                continue
            for w, nei in adj[node]:
                nd = d + w
                if nd < dists[nei]:
                    dists[nei] = nd
                    heapq.heappush(heap, (nd, nei))

        tot = max(dists.values())
        return tot if tot != float('inf') else -1