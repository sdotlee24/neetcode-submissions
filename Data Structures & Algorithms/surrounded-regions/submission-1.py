class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def validate(i, j):
            #bfs
            q = deque()
            visited = set()
            visited.add((i, j))
            q.append((i, j))
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                        return False
                    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dir_i, dir_j in dir:
                        newI = i + dir_i
                        newJ = j + dir_j
                        if newI < 0 or newJ < 0 or newI >= len(board) or newJ >= len(board[0]) or (newI, newJ) in visited or board[newI][newJ] != 'O':
                            continue
                        q.append((newI, newJ))
                        visited.add((newI, newJ))
            return True

        def fill(i, j):
            #bfs
            q = deque()
            q.append((i, j))
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    board[i][j] = 'X'
                    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dir_i, dir_j in dir:
                        newI = i + dir_i
                        newJ = j + dir_j
                        if newI < 0 or newJ < 0 or newI >= len(board) or newJ >= len(board[0]) or board[newI][newJ] != 'O':
                            continue
                        q.append((newI, newJ))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and validate(i, j):
                    fill(i, j)



        