class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memo = defaultdict(int)
        max_count = 0
        res = 0
        i = 0
        
        for j in range(len(s)):
            memo[s[j]] += 1
            max_count = max(max_count, memo[s[j]])
            
            # If window is invalid (more than k changes needed), shrink from left
            if (j - i + 1) - max_count > k:
                memo[s[i]] -= 1
                i += 1
            
            res = max(res, j - i + 1)
        
        return res

