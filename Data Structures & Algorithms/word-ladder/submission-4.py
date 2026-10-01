class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        words = wordList + [beginWord]

        adjList = defaultdict(list)

        def withinOne(a, b):
            diffs = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diffs += 1

            return diffs == 1
        # built adj list connecting reachable words
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if withinOne(words[i], words[j]):
                    adjList[words[i]].append(words[j])
                    adjList[words[j]].append(words[i])
        
        visited = set()
        q = deque()
        res = 1
        visited.add(beginWord)
        q.append(beginWord)

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for w in adjList[word]:
                    if w not in visited:
                        q.append(w)
                        visited.add(w)
            res += 1
        return 0