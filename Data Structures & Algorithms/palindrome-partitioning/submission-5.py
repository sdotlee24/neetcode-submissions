class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(idx, cur):
            if idx == len(s):
                res.append(cur.copy())
                return
            
            for i in range(idx, len(s)):
                temp = s[idx:i+1]
                if isPalindrome(temp):
                    cur.append(temp)
                    dfs(i+1, cur)
                    cur.pop()

        def isPalindrome(s):
            return s[::-1] == s

        dfs(0, [])
        return res