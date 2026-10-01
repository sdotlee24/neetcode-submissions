class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        lastEnd = intervals[0][1]

        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= lastEnd:
                res[-1] = [res[-1][0], max(lastEnd, end)]
            else:
                res.append([start, end])
            lastEnd = max(lastEnd, end)
        return res