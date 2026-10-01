class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def satisfiesCriteria(word1, word2):
            diffs = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diffs += 1

            return diffs == 1
        
        words = wordList + [beginWord]
        tree = defaultdict(list)
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if satisfiesCriteria(words[i], words[j]):
                    tree[words[i]].append(words[j])
                    tree[words[j]].append(words[i])
        
        if endWord not in words:
            return 0
        
        q = deque([(beginWord, 1)])
        visited = set()
        while q:
            w, dist = q.popleft()
            if w == endWord:
                return dist
            for child in tree[w]:
                if child not in visited:
                    visited.add(child)
                    q.append((child, dist+1))
        
        return 0
        