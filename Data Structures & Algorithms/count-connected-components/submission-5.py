class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {}
        height = {}
        for i in range(n):
            par[i] = i
            height[i] = 0

        def find(c):
            p = par[c]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False

            if height[pa] < height[pb]:
                pa, pb = pb, pa
            par[pb] = pa
            if height[pa] == height[pb]:
                height[pa] += 1
            return True

        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1

        return res