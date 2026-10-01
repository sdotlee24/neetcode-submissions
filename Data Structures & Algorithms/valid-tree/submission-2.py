class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        al = defaultdict(list)
        for a, b in edges:
            al[a].append(b)
            al[b].append(a)
        
        visited = set()
        def traverse(k, prev):
            if k in visited:
                return False
            
            visited.add(k)
            for b in al[k]:
                if b != prev:
                    if not traverse(b, k):
                        return False
            return True

        return traverse(0, -1) and len(visited) == n
