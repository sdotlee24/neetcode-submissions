class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def traverse(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            if text1[i1] == text2[i2]:
                val = 1 + traverse(i1+1, i2+1)
                memo[(i1, i2)] = val
                return val
            newVal = max(traverse(i1+1, i2), traverse(i1, i2+1))
            memo[(i1, i2)] = newVal
            return newVal
        

        return traverse(0, 0)