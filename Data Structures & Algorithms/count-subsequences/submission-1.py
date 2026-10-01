class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def traverse(i, j):
            if j == len(t):
                return 1  # matched all of t — one valid way
            if i == len(s):
                return 0  # ran out of s before finishing t
            if (i, j) in memo:
                return memo[(i, j)]

            skip = traverse(i+1, j)  # don't use s[i]
            use = 0
            if s[i] == t[j]:
                use = traverse(i+1, j+1)

            memo[(i, j)] = skip + use
            return memo[(i, j)]

        return traverse(0, 0)