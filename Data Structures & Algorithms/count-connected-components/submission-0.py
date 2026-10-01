class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        al = defaultdict(list)
        for a, b in edges:
            al[a].append(b)
            al[b].append(a)
        
        res = 0
        visited = set()
        def traverse(k, prev):
            if k in visited or al[k] == []:
                return
            visited.add(k)
            for a in al[k]:
                if a == prev:
                    continue
                traverse(a, k)
        
        for k in range(n):
            if k not in visited:
                traverse(k, -1)
                res += 1
        
        return res
