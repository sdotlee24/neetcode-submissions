class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        result = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                result = max(result, len(seen))
            else:
                
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            
        return result


