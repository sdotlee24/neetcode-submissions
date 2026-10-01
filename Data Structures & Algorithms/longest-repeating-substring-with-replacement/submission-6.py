class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        count = 0
        mostIdentical = 0

        charMap = defaultdict(int)
        l = 0
        for r in range(len(s)):
            charMap[s[r]] += 1
            mostIdentical = max(mostIdentical, charMap[s[r]])
            while (r-l+1 > k + mostIdentical):
                charMap[s[l]] -= 1
                l += 1
                mostIdentical = max(mostIdentical, max(charMap.values()))
            
            res = max(res, r-l+1)
        return res