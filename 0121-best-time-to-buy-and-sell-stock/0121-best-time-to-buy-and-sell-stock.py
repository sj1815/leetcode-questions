class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in range(len(prices)):
            if prices[price] < min_price:
                min_price = prices[price]
            elif prices[price] - min_price > max_profit:
                max_profit = prices[price] - min_price
        
        return max_profit
        