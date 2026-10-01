"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        if not intervals:
            return 0
        res = [intervals[0].end]

        for sch in intervals[1:]:
            start = sch.start
            end = sch.end
            hasNoConflicts = False
            for i in range(len(res)):
                if res[i] <= start:
                    res[i] = max(res[i], end)
                    hasNoConflicts = True
                    break
            if not hasNoConflicts:
                res.append(end)
        
        return len(res)



