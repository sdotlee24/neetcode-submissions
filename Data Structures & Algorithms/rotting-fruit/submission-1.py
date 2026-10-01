class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numFruits = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    numFruits += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        res = 0
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            if numFruits == 0:
                return res
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIR:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        numFruits -= 1
                        grid[nr][nc] = 2
            res += 1
        
        return res if not numFruits else -1