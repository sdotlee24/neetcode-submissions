"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        endTimes = []
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return 0
        heapq.heapify(endTimes)
        heapq.heappush(endTimes, intervals[0].end)

        for i in intervals[1:]:
            if i.start < endTimes[0]:
                heapq.heappush(endTimes, i.end)
            else:
                heapq.heappushpop(endTimes, i.end)
        
        return len(endTimes)