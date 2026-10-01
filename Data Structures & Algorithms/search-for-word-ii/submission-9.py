class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.append(w)
        res = []
        def traverse(i, j, node):
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] not in node.children:
                return
            node = node.children[board[i][j]]
            if node.endOfWord:
                res.append(node.word)
                node.endOfWord = False
            temp = board[i][j]
            board[i][j] = "#"
            dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in dir:
                newR, newC = dr+i, dc+j
                traverse(newR, newC, node)
            board[i][j] = temp
        for r in range(len(board)):
            for c in range(len(board[0])):
                traverse(r,c,trie.node)
        
        return res


class Trie:
    def __init__(self) -> None:
        self.node = TrieNode()
    
    def append(self, word):
        trie = self.node
        for w in word:
            if w not in trie.children:
                trie.children[w] = TrieNode()
            trie = trie.children[w]
        trie.endOfWord = True
        trie.word = word

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False
        self.word = ""