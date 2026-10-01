class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        par = {}
        height = {}
        N = len(edges)
        
        for i in range(1, N+1):
            par[i] = i
            height[i] = 0
        
        def find(k):
            p = par[k]
            while par[p] != p:
                par[p] = par[par[p]]
                p = par[p]
            
            return p
        
        def union(a, b):
            par_a, par_b = find(a), find(b)
            if par_a == par_b:
                return False
            
            if height[par_a] < height[par_b]:
                par_a, par_b = par_b, par_a
            par[par_b] = par_a
            if height[par_a] == height[par_b]:
                height[par_a] += 1
            return True
        
        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]