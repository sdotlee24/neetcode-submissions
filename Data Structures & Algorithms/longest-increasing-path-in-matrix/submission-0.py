class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}

        def traverse(r, c, prev):
            if not 0 <= r < len(matrix) or not 0 <= c < len(matrix[0]) or matrix[r][c] <= prev:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            
            prev = matrix[r][c]
            longPath = max(traverse(r,c+1, prev), traverse(r,c-1, prev), 
            traverse(r+1,c, prev), traverse(r-1,c, prev)) + 1
            memo[(r,c)] = longPath

            return longPath
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, traverse(i, j, -1))
        return res