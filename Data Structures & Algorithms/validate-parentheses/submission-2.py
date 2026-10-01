class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']' : '['}
        for r in s:
            if r in ['(', '[', '{']:
                stack.append(r)
            else:
                if len(stack) == 0:
                    return False
                l = stack.pop()
                if l != matching[r]:
                    return False        
        return len(stack) == 0

