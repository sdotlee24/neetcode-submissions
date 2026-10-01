class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque()
        carry = 1
        for v in digits[::-1]:
            temp = carry + v
            if temp == 10:
                temp = 0
            else:
                carry = 0
            res.appendleft(temp)
        if carry:
            res.appendleft(carry)
        
        return list(res)