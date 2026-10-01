class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            while q:
                for i in range(len(q)):
                    curR, curC = q.popleft()
                    grid[curR][curC] = "0"
                    DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for dr, dc in DIR:
                        newR, newC = dr + curR, dc + curC
                        if (0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and
                        grid[newR][newC] == "1"):
                            grid[newR][newC] = "0"
                            q.append((newR, newC))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        return res