class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate, maxRate = 1, max(piles)
        res = 0
        while minRate <= maxRate:
            atQ = (minRate + maxRate) // 2
            tries = 0
            for n in piles:
                tries += math.ceil(float(n) / atQ)
            if tries <= h:
                maxRate = atQ - 1
                res = atQ
            else:
                minRate = atQ + 1
        
        return res
        