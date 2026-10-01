class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(idx, cur):
            if idx == len(word):
                return cur.word
            if word[idx] == '.':
                for c in cur.children:
                    if dfs(idx + 1, cur.children[c]):
                        return True
                return False
            else:
                if word[idx] not in cur.children:
                    return False
                return dfs(idx + 1, cur.children[word[idx]])
        return dfs(0, self.root)


class Trie:
    def __init__(self):
        self.word = False
        self.children = {}