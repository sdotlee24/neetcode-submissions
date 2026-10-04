class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        lastDay = max(days)

        def traverse(i):
            if i == len(days):
                return 0
            if i in memo:
                return memo[i]
            
            curDay = days[i]
            # 1 day pass
            minCost = traverse(i+1) + costs[0]

            # 7 day pass
            newDay = curDay + 7
            j = i
            while j < len(days) and newDay > days[j]:
                j += 1
            minCost = min(minCost, traverse(j) + costs[1])
            
            newDay = curDay + 30
            j = i
            while j < len(days) and newDay > days[j]:
                j += 1
            minCost = min(minCost, traverse(j) + costs[2])
            memo[i] = minCost
            return minCost
        return traverse(0)


# BOTTOM UP SOLUTION NEXT, FOLLOW SAME PATTERN AS TOP DOWN APPROACH HERE!