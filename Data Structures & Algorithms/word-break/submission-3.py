class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def backtrack(idx):
            if idx == len(s):
                return True
            if idx in memo:
                return memo[idx]
            for i in range(idx, len(s)):
                if s[idx:i+1] in wordDict:
                    if backtrack(i+1):
                        memo[idx] = True
                        return True
            memo[idx] = False
            return False
        
        return backtrack(0)