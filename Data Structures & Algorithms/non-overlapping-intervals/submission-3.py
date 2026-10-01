class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: x[0])
        temp = intervals[0]

        for start, end in intervals[1:]:
            if start < temp[1]:
                temp[1] = min(temp[1], end)
                count += 1
            else:
                temp = [start, end]
        
        return count