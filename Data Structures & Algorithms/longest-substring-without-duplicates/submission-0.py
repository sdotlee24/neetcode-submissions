class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #zxyzxy
        result = 0 
        memo = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] in memo:
                result = max(result, len(memo))
                while s[r] in memo:
                    memo.remove(s[l])
                    l += 1
            else:
                memo.add(s[r])
                r += 1
                result = max(result, len(memo))
        
        return result