class Solution:
    def reverseBits(self, n: int) -> int:
        multi = 31
        res = 0
        while multi >= 0:
            if n & 1:
                res += 2 ** multi
            multi -= 1
            n >>= 1
        
        return res