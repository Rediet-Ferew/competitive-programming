class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        dp = [0]
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                dp.append(0)
            else:
                diff = prices[r] - prices[l]
                if diff > dp[-1]:
                    dp[-1] = diff
                    r += 1
                else:
                    l = r
                    r += 1
                    dp.append(0)
                    
        return sum(dp)