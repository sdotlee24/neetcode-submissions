class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        #goal is to connect minimum elemnts first
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            temp = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += temp
            heapq.heappush(sticks, temp)
        return cost
