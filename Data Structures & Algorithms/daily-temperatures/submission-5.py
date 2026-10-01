class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stck = []
        for i in range(len(temperatures)):
            while len(stck) > 0 and stck[-1][0] < temperatures[i]:
                temp, idx = stck.pop()
                res[idx] = i - idx

            stck.append((temperatures[i], i))
        return res