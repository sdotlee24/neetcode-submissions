class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for a, b in edges:
            if not uf.union(a, b):
                return [a, b]
        




class UnionFind():
    def __init__(self, n) -> None:
        self.par = {}
        self.rank = {}
        for i in range(1, n+1):
            self.par[i] = i
            self.rank[i] = 0
    def find(self, node):
        p = self.par[node]
        while p != self.par[p]:
            p = self.par[p]
        
        return p
    
    def union(self, a, b):
        parA, parB = self.find(a), self.find(b)
        if parA == parB:
            return False
        if self.rank[parA] > self.rank[parB]:
            self.par[parB] = parA
        elif self.rank[parB] > self.rank[parA]:
            self.par[parA] = parB
        else:
            self.par[parB] = parA
            self.rank[parA] += 1
    
        return True