class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        max_piles = []

        for pile in piles:
            heapq.heappush(max_piles, -pile)
        
        while k > 0:

            val = -1*(heapq.heappop(max_piles))
            rem = val // 2
            heapq.heappush(max_piles, -1*(val - rem))
            k -= 1

        total = 0
        for num in max_piles:
            total -= num
       
        return total