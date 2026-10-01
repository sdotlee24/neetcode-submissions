class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(word):
            return word == word[::-1]
        
        def dfs(cur, idx):
            if idx == len(s):
                if isPalindrome(cur[-1]):
                    res.append(cur[:])
                return
            temp = cur[-1]
            cur[-1] += s[idx]
            dfs(cur, idx+1)
            cur[-1] = temp
            if isPalindrome(cur[-1]):
                dfs(cur + [s[idx]], idx+1)

        dfs([s[0]], 1)

        return res