class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        temp = intervals[0]
        res = []
        for start, end in intervals[1:]:
            if start <= temp[1]:
                temp[0] = min(temp[0], start)
                temp[1] = max(temp[1], end)
            else:
                res.append(temp)
                temp = [start, end]
        
        res.append(temp)
        return res