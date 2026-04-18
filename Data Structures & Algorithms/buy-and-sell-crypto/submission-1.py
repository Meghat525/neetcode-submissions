class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_profit = 0
        l = 0
        r = 1
        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            if curr_profit > max_profit:
                max_profit = curr_profit
            if prices[l] > prices[r]:
                l = r
            r += 1
        return max_profit