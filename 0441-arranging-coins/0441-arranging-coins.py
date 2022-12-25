class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 1
        total = 0
        while total <= n:
            total += k
            k += 1
        return k - 2