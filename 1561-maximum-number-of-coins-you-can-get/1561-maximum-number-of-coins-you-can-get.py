class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        summation = 0
        for i in range(len(piles) - 2, (len(piles)//3) - 1 , -2):
            summation += piles[i]
        return summation