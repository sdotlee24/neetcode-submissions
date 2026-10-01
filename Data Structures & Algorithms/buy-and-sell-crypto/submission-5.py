class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b = 0
        for s in range(len(prices)):
            if prices[s] < prices[b]:
                b = s
            profit = max(profit, prices[s]-prices[b])
        return profit