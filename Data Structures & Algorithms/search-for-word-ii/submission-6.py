class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie of all words
        root = Trie()
        for w in words:
            self.insertTrie(w, root)

        # do dfs on board, while iterating through the trie as well
        res = []
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def dfs(r, c, trie, cur):
            if trie.word:
                trie.word = False
                res.append(''.join(cur))
            for dx, dy in DIR:
                newR, newC = r + dx, c + dy
                if (0 <= newR < len(board) and 0 <= newC < len(board[0]) and 
                (newR, newC) not in visited and board[newR][newC] in trie.children):
                    cur.append(board[newR][newC])
                    visited.add((newR, newC))
                    dfs(newR, newC, trie.children[board[newR][newC]], cur)
                    cur.pop()
                    visited.remove((newR, newC))
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.children:
                    visited.add((r, c))
                    dfs(r, c, root.children[board[r][c]], [board[r][c]])
                    visited.remove((r, c))
        return res
    def insertTrie(self, word, trie):
        for w in word:
            if w not in trie.children:
                trie.children[w] = Trie()
            trie = trie.children[w]
        trie.word = True


class Trie:
    def __init__(self) -> None:
        self.word = False
        self.children = {}