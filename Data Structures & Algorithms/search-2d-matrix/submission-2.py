class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(i, j):
            m = (i + j) // 2
            r = m // len(matrix[0])
            c = m % len(matrix[0])
            if i > j:
                return False
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                return search(i, m-1)
            return search(m+1, j)




        return search(0, len(matrix) * len(matrix[0]) - 1)