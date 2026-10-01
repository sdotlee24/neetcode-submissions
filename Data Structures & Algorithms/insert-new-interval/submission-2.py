class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:
            # Case 1: current interval ends before newInterval starts → no overlap
            if interval[1] < newInterval[0]:
                res.append(interval)
            
            # Case 2: current interval starts after newInterval ends → no overlap,
            # but newInterval comes first
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval  # treat this as the new "to place" interval
            
            # Case 3: overlap → merge into newInterval
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]
        
        # add the last remaining interval
        res.append(newInterval)
        return res