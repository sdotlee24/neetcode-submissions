class Solution:
    def myPow(self, x: float, n: int) -> float:
        def traverse(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            temp = traverse(x, n // 2)
            temp *= temp
            if n % 2:
                temp *= x
            
            return temp
        res = traverse(x, abs(n))

        return res if n > 0 else 1 / res