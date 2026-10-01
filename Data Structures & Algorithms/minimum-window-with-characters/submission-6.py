class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        tMap = defaultdict(int)
        for c in t:
            tMap[c] += 1
        
        charMap = defaultdict(int)
        l = 0
        res = ""
        minSize = len(s) + 1
        have = 0
        need = len(tMap)
        for r in range(len(s)):
            charMap[s[r]] += 1
            if tMap[s[r]] == charMap[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < minSize:
                    minSize = r-l+1
                    res = s[l:r+1]
                if charMap[s[l]] == tMap[s[l]]:
                    have -= 1
                charMap[s[l]] -= 1
                l += 1
        
        return res