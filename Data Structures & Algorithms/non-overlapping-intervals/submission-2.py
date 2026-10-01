class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < end:
                res += 1
                end = min(end, interval[1])
            else:
                end = max(end, interval[1])
        return res