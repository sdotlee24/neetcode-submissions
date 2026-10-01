class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals) - 1
        while l <= r:
            m = (l + r) // 2
            if intervals[m][0] < newInterval[0]:
                l = m + 1
            else:
                r = m - 1
        
        intervals.insert(l, newInterval)
        temp = intervals[0]
        res = []
        for start, end in intervals[1:]:
            if start <= temp[1]:
                temp[1] = max(temp[1], end)
            else:
                res.append(temp)
                temp = [start, end]
        res.append(temp)

        return res