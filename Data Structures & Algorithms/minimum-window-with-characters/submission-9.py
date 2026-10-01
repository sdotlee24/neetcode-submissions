class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        sMap = defaultdict(int)
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        
        l = 0
        resLen = len(s) + 1
        left = len(tMap.keys())
        resL = 0
        resR = -1
        for r in range(len(s)):
            sMap[s[r]] += 1
            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                left -= 1
            while left == 0 and l <= r:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    resL, resR = l, r
                if s[l] in tMap and sMap[s[l]] == tMap[s[l]]:
                    left += 1
                sMap[s[l]] -= 1
                l += 1
        
        return s[resL:resR+1]