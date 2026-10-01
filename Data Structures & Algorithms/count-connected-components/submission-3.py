class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tree = defaultdict(list)
        for e1, e2 in edges:
            tree[e1].append(e2)
            tree[e2].append(e1)
        
        res = 0
        visited = set()
        def traverse(k, prev):
            if k in visited or tree[k] == []:
                return

            visited.add(k)
            for child in tree[k]:
                if child != prev:
                    traverse(child, k)
        

        for k in range(n):
            if k not in visited:
                traverse(k, -1)
                res += 1
        return res
