class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        from collections import deque
        
        rows, cols = len(board), len(board[0])
        
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            board[i][j] = 'E'      # mark as safe
            
            while q:
                size = len(q)
                for _ in range(size):
                    x, y = q.popleft()
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'O':
                            board[nx][ny] = 'E'
                            q.append((nx, ny))

        # 1. Call BFS from all boundary O's
        for i in range(rows):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][cols - 1] == 'O':
                bfs(i, cols - 1)

        for j in range(cols):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[rows - 1][j] == 'O':
                bfs(rows - 1, j)

        # 2. Flip all remaining O → X, and E → O
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
