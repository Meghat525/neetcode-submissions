class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_price = prices[0]
        max_price_arr = []
        for i in range(len(prices)):
            if prices[i] < least_price:
                least_price = prices[i]
            max_price_arr.append(prices[i] - least_price)

        return max(0, max(max_price_arr))