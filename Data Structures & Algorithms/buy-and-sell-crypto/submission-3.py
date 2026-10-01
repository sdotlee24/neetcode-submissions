class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b, s = 0, 1

        while s < len(prices):
            if prices[b] > prices[s]:
                b = s
            else:
                profit = max(profit, prices[s] - prices[b])
            s += 1
        return profit
