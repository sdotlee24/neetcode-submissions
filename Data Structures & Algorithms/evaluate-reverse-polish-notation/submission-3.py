class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op  = ['+', '-', '*', '/']
        stck = []
        for t in tokens:
            if t in op:
                two = stck.pop()
                one = stck.pop()
                if t == '+':
                    stck.append(one + two)
                elif t =='-':
                    stck.append(one - two)
                elif t == '*':
                    stck.append(one * two)
                elif t =='/':
                    stck.append(int(one / two))
            else:
                stck.append(int(t))
        
        return stck[0]
