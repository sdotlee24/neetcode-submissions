class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0

        def traverse(r, c):
            q = deque()
            q.append((r, c))
            size = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    size += 1
                    DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for dr, dc in DIR:
                        newR, newC = r + dr, c + dc
                        if (0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and
                        grid[newR][newC] != 0):
                            grid[newR][newC] = 0
                            q.append((newR, newC))
            return size
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    maxSize = max(maxSize, traverse(i, j))
        return maxSize