class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r + 1
        while l <= r:
            m = (l + r) // 2
            tries = 0
            for n in piles:
                tries += math.ceil(float(n) / m)
            
            if tries > h:
                l = m + 1
            else:
                r = m - 1
                res = min(res, m)
        
        return res