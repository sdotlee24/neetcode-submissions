class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ['+', '-', '/', '*']:
                stack.append(int(t))
            else:
                l2 = stack.pop()
                l1 = stack.pop()
                if t == '+':
                    stack.append(l1 + l2)
                elif t == '-':
                    stack.append(l1 - l2)
                elif t == '/':
                    sign = 1 if l2 * l1 >= 0 else -1
                    magnitude = abs(l1) // abs(l2)
                    stack.append(sign * magnitude)
                else:
                    stack.append(l1 * l2)
        
        return stack[0]