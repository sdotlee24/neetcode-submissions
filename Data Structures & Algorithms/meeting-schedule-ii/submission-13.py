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
        ends = [intervals[0].end]
        heapq.heapify(ends)
        for itv in intervals[1:]:
            if itv.start < ends[0]:
                heapq.heappush(ends, itv.end)
            else:
                heapq.heappushpop(ends, itv.end)
        
        return len(ends)

