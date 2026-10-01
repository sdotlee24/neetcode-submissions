class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        seenChars = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            seenChars[s[r]] += 1
            while len(seenChars) > k:
                seenChars[s[l]] -= 1
                if seenChars[s[l]] == 0:
                    del seenChars[s[l]]
                l += 1
            res = max(res, r-l+1)
        
        return res