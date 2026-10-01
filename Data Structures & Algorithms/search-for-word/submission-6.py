class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, idx):
            if idx == len(word) - 1:
                return True  # last character already matched at entry

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and board[nr][nc] == word[idx + 1]):
                    visited.add((nr, nc))
                    if dfs(nr, nc, idx + 1):
                        return True
                    visited.remove((nr, nc))  # backtrack

            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(i, j, 0):
                        return True
                    visited.remove((i, j))
        return False