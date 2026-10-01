class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = defaultdict(list)
        for e1, e2 in edges:
            tree[e1].append(e2)
            tree[e2].append(e1)
                
        visited = [0] * n

        def traverse(edge, parent):
            if visited[edge] == 1:
                return False
            if visited[edge] == 2:
                return True
            
            visited[edge] = 1
            for child in tree.get(edge, []):
                if child == parent:
                    continue
                if not traverse(child, edge):
                    return False
            
            visited[edge] = 2
            return True
        
        if not traverse(0, -1):
            return False
        for v in visited:
            if v == 0:
                return False
        return True
            