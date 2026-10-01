class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        for v in digits[::-1]:
            temp = carry + v
            if temp == 10:
                temp = 0
            else:
                carry = 0
            res.append(temp)
        if carry:
            res.append(carry)
        res.reverse()
        return res