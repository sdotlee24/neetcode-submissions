class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures) - 1):
            j = i + 1
            while j < len(temperatures) and temperatures[i] >= temperatures[j]:
                j += 1
            if j < len(temperatures):
                res.append(j-i)
            else:
                res.append(0)
        
        res.append(0)

        return res