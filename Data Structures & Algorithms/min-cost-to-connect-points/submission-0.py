class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        res = 0
        # Build every possible edge
        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)

                edges.append((distance, i, j))

        # Sort edges by increasing distance
        edges.sort()

        uf = UnionFind(n)
        
        for i in range(len(edges)):
            dist, a, b = edges[i]
            if uf.union(a, b):
                res += dist
        
        return res

class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.height = {}
        for i in range(n):
            self.par[i] = i
            self.height[i] = 0
    
    def find(self, node):
        p = self.par[node]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p
    def union(self, a, b):
        parA, parB = self.find(a), self.find(b)
        if parA == parB:
            return False
        
        if self.height[parA] < self.height[parB]:
            parA, parB = parB, parA
        
        self.par[parB] = parA
        if self.height[parA] == self.height[parB]:
            self.height[parA] += 1
        return True
