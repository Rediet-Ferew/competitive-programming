class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        n = len(coins)
        
        def backtrack(idx, amt):
            if idx == n - 1:
                if amt % coins[idx] == 0:
                    return amt//coins[idx]
                else:
                    return float('inf')
            if (idx, amt) in memo:
                return memo[(idx, amt)]
            not_choose = 0 + backtrack(idx + 1, amt)
          
            choose = float("inf")
            if coins[idx] <= amt:
                
                choose = 1 + backtrack(idx, amt - coins[idx])
                
            
            memo[(idx, amt)] = min(not_choose, choose)
            return memo[(idx, amt)]
        change = backtrack(0, amount)
        if change == float("inf"):
            return -1
        else:
            return change