class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def winnerFinder(n, k):
            if n == 1:
                return 0
            return (winnerFinder(n - 1, k) + k) % n
        
        winner = winnerFinder(n, k)
        
        return winner + 1