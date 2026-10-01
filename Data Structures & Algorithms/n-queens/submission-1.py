class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, diag1, diag2 = set(), set(), set()  # diag1: row-col, diag2: row+col

        def dfs(layer, cur):
            if layer == n:
                res.append(cur.copy())
                return

            for i in range(n):
                if i in cols or (layer - i) in diag1 or (layer + i) in diag2:
                    continue

                curLayer = ['.'] * n
                curLayer[i] = 'Q'
                cols.add(i)
                diag1.add(layer - i)
                diag2.add(layer + i)
                cur.append(''.join(curLayer))

                dfs(layer + 1, cur)

                cur.pop()
                cols.remove(i)
                diag1.remove(layer - i)
                diag2.remove(layer + i)

        dfs(0, [])
        return res