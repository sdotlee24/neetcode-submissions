class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def traverse(i, j):
            if i >= len(word1) or j >= len(word2):
                return max(len(word1)-i, len(word2)-j)
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                val = traverse(i+1, j+1)
                memo[(i, j)] = val
                return val
            val = 1 + min(traverse(i+1, j+1), traverse(i, j+1), traverse(i+1, j))
            memo[(i, j)] = val
            return val

        return traverse(0, 0)