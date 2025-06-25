class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        
        min_price = float('inf')
        max_profit = 0        
        
        for price in prices:
            profit = price - min_price
            
            min_price = min(price, min_price)
            max_profit = max(profit, max_profit)
                
        return max_profit
