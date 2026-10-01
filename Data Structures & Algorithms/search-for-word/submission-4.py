class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r, c, idx, visited):
            if idx == len(word) - 1 and word[idx] == board[r][c]:
                return True
            if idx >= len(word) or board[r][c] != word[idx]:
                return False
            
            
            d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in d:
                if not ((r+dr, c+dc) in visited or r + dr < 0 or c + dc < 0 or r + dr >= len(board) or c + dc >= len(board[0])):
                    visited.add((r, c))
                    found = dfs(r + dr, c + dc, idx+1, visited)
                    if found:
                        return True
                    visited.remove((r, c))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, set()):
                    return True
        return False