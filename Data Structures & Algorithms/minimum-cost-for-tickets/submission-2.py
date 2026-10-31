class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        lastDay = max(days)

        def traverse(i):
            if i == len(days):
                return 0
            if i in memo:
                return memo[i]
            
            #1 day
            cost = traverse(i+1) + costs[0]

            #7 day
            nextIdx = i+1
            while nextIdx < len(days) and days[nextIdx] < days[i] + 7:
                nextIdx += 1
            cost = min(cost, traverse(nextIdx) + costs[1])
            # 30 days
            nextIdx = i+1
            while nextIdx < len(days) and days[nextIdx] < days[i] + 30:
                nextIdx += 1
            cost = min(cost, traverse(nextIdx) + costs[2]) 

            memo[i] = cost
            return cost
        return traverse(0)
