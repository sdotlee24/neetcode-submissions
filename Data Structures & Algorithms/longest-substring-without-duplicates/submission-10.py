class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        seen = set()

        res = 0
        for n in s:
            while n in seen:
                seen.remove(s[i])
                i += 1
            seen.add(n)
            res = max(res, len(seen))

        return res


