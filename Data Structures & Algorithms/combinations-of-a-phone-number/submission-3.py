class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(idx, cur):
            if idx == len(digits):
                res.append(cur)
                return
            
            for c in digitToChar[digits[idx]]:
                dfs(idx+1, cur+c)
        if digits:
            dfs(0, "")
        return res