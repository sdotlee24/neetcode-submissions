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
                cur.append(s[idx])
                dfs(cur, idx+1)
                cur.pop()  # we need to pop, since "cur" is a reference to array (same array is accessed by whole stack)

        dfs([s[0]], 1)

        return res