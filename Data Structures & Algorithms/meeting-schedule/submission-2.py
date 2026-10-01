"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return True
        prevEnd = intervals[0].end

        for sch in intervals[1:]:
            if sch.start < prevEnd:
                return False
            prevEnd = sch.end
        return True