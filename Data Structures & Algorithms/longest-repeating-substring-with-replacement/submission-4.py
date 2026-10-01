class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #length of substring - # of most frequent char in substring <= k = characters to replace
        #charOccurenceMap: {"a": 0}
        #most frequenct char in substring
        charMap = {}

        l = 0
        maxf = 0
        res = 0
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            maxf = max(maxf, charMap[s[r]])

            while r-l+1 - maxf > k:
                charMap[s[l]] -= 1
                l += 1
                maxf = max(charMap.values())
            res = max(res, r-l+1)
        return res

            
            

