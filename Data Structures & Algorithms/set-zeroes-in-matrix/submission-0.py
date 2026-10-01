class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        #brute force solution: O(n^2 space, n^2 time)
        coords = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    coords.append((i, j))
        
        for i, j in coords:
            for n in range(len(matrix[0])):
                matrix[i][n] = 0
            for n in range(len(matrix)):
                matrix[n][j] = 0
        
        