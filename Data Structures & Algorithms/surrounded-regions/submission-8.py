class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #replace everything thqat isnt surroundable with ?, via bfs
        q = deque()
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1):
                    q.append((i,j))
                    board[i][j] = '?'
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in DIR:
                    nr,nc = dr+r,dc+c
                    if (0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 'O'):
                        q.append((nr,nc))
                        board[nr][nc] = '?'
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '?':
                    board[i][j] = 'O'