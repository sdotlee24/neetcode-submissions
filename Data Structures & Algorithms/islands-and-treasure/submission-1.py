class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        steps = 1
        q = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIR:
                    newR, newC = r+dr, c+dc
                    if (0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and
                    (newR, newC) not in visited and grid[newR][newC] > 0):
                        visited.add((newR, newC))
                        q.append((newR, newC))
                        grid[newR][newC] = min(grid[newR][newC], steps)
            steps += 1
        

                    