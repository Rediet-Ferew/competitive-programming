class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # buy or sell at each day
        # 
        memo = {}
        def dp(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in memo:
                return memo[(i, buy)]
            
            if buy:
               
                val_1 = dp(i + 1, not buy) - prices[i]
                val_2 = dp(i + 1, buy)
                memo[(i, buy)] = max(val_1, val_2)
            else:
                val_1 = dp(i + 1, not buy) + (prices[i] - fee)
                val_2 = dp(i + 1, buy)
                memo[(i, buy)] = max(val_1, val_2)
            
            return memo[(i, buy)]
        
        return dp(0, True)