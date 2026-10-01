class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def compute(dig):
            res = 0
            while dig > 0:
                res += (dig % 10) ** 2
                dig = dig // 10
            return res
        
        val = compute(n)
        while val not in seen:
            seen.add(val)
            if val == 1:
                return True
            val = compute(val)
        return False