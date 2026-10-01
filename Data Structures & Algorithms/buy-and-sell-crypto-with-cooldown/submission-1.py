class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}


        def traverse(buying, i):
            if i >= len(prices):
                return 0
            if (buying, i) in memo:
                return memo[(buying, i)]

            nothing = traverse(buying, i+1)
            if buying:
                buy = traverse(False, i+1) - prices[i]
                memo[(buying, i)] = max(buy, nothing)
            else:
                sell = traverse(True, i+2) + prices[i]
                memo[(buying, i)] = max(sell, nothing)
            
            return memo[(buying, i)]
        return traverse(True, 0)