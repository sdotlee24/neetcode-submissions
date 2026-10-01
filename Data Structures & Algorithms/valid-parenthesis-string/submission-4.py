class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = {}
        def traverse(i, depth):
            key = (i, depth)
            if key in memo:
                return memo[key]
            idx, d = i, depth
            while idx < n:
                c = s[idx]
                if c == '*':
                    c1 = traverse(idx+1, d)
                    c2 = traverse(idx+1, d+1)
                    c3 = d > 0 and traverse(idx+1, d-1)
                    result = c1 or c2 or c3
                    memo[key] = result
                    return result
                elif c == '(':
                    d += 1
                else:
                    if d > 0:
                        d -= 1
                    else:
                        memo[key] = False
                        return False
                idx += 1
            result = (d == 0)
            memo[key] = result
            return result
        return traverse(0, 0)