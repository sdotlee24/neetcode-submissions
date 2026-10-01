class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            temp = i
            count = 0
            while temp:
                count += temp & 1
                temp >>= 1
            res.append(count)
        return res