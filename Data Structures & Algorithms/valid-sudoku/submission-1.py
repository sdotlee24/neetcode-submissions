class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            seen = set()
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        for c in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        for r in range(3):
            for c in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        dr = r * 3 + i
                        dc = c * 3 + j
                        if board[dr][dc] == ".":
                            continue
                        if board[dr][dc] in seen:
                            return False
                        seen.add(board[dr][dc])
        return True