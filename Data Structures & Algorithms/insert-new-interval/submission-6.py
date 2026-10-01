class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Insert newInterval into the right place (list stays sorted)
        l, r = 0, len(intervals) - 1
        while l <= r:
            m = (l + r) // 2
            if intervals[m][0] < newInterval[0]:
                l = m + 1
            else:
                r = m - 1
        
        intervals.insert(l, newInterval)

        # Standard merge
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res