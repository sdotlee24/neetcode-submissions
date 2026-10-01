class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # attach original index before sorting
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key=lambda x: x[2])

        def mst(skip=-1, force=-1):
            uf = UnionFind(n)
            total, count = 0, 0
            if force != -1:
                u, v, w, _ = edges[force]
                uf.union(u, v)
                total, count = w, 1
            for j, (u, v, w, _) in enumerate(edges):
                if j == skip:
                    continue
                if uf.union(u, v):
                    total += w
                    count += 1
            return total if count == n - 1 else float('inf')

        base = mst()
        res = [[], []]
        for j, (_, _, _, idx) in enumerate(edges):
            if mst(skip=j) > base:
                res[0].append(idx)
            elif mst(force=j) == base:
                res[1].append(idx)
        return res


class UnionFind:
    def __init__(self, n) -> None:
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, a):
        if self.par[a] != a:
            self.par[a] = self.find(self.par[a])
        return self.par[a]

    def union(self, a, b):
        parA, parB = self.find(a), self.find(b)
        if parA == parB:
            return False
        if self.rank[parA] > self.rank[parB]:
            self.par[parB] = parA
        else:
            if self.rank[parA] == self.rank[parB]:
                self.rank[parB] += 1
            self.par[parA] = parB
        return True