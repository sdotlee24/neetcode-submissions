class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def bfs(q):
            candidates = set(q)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in DIR:
                        nr, nc = dr+r, dc+c
                        if (0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and (nr, nc) not in candidates
                        and heights[nr][nc] >= heights[r][c]):
                            candidates.add((nr,nc))
                            q.append((nr,nc))
            return candidates
        pacific = deque()
        atlantic = deque()
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or (c == 0 and r != 0):
                    pacific.append((r, c))
                if r == len(heights)-1 or (c == len(heights[0])-1 and r != len(heights)-1):
                    atlantic.append((r, c))
        pacset = bfs(pacific)
        atset = bfs(atlantic)

        return list(pacset.intersection(atset))
