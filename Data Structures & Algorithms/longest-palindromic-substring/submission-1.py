class Solution:
    def longestPalindrome(self, s: str) -> str:
        topCount = 0
        res = ""
        for i in range(0, len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > topCount:
                    topCount = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        for i in range(1, len(s)):
            l, r = i-1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > topCount:
                    topCount = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
