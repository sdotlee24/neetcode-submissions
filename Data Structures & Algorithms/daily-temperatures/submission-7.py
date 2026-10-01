class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [7, 2, 4, 3, 8] [7, 2] (4) -> [7, 3]
        # [4, 1, 2, 1, 0]

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) != 0 and stack[-1][0] < temperatures[i]:
                val, idx = stack.pop()
                res[idx] = i-idx
            
            stack.append([temperatures[i], i])

        return res