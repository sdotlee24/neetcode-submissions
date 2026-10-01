class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        for i in range(32):
            res += ((a & 1) ^ (b & 1) ^ carry) << i
            if a & 1 & b & 1 or ( a ^ b) & carry:
                carry = 1
            else:
                carry = 0
            a >>= 1
            b >>= 1
        if res > 0x7FFFFFFF:
            res -= (1 << 32)
        return res
