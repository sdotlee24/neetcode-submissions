class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(i, j):
            #bfs
            q = deque()
            q.append((i, j))
            board[i][j] = 'E'
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    board[i][j] = 'E'
                    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dir_i, dir_j in dir:
                        newI = i + dir_i
                        newJ = j + dir_j
                        if newI < 0 or newJ < 0 or newI >= len(board) or newJ >= len(board[0]) or board[newI][newJ] != 'O':
                            continue
                        q.append((newI, newJ))
            
        for i in range(len(board)):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][len(board[0]) - 1] == 'O':
                bfs(i, len(board[0]) - 1)

        for i in range(len(board[0])):
            if board[0][i] == 'O':
                bfs(0, i)
            if board[len(board) - 1][i] == 'O':
                bfs(len(board) - 1, i)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
            
            



        