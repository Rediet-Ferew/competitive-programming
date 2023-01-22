class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        n = len(piles)
        piles.sort()
        max_coins = 0
        bobs = n // 3
        
        for idx in range(n - 2, bobs - 1, -2):
            
            max_coins += piles[idx]
        
        return max_coins