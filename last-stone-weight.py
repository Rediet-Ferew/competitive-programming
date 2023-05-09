class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_ = []

        for num in stones:
            heapq.heappush(stones_, -num)
        
        while len(stones_) > 1:
            x = -1 * (heapq.heappop(stones_))
            y = -1 * (heapq.heappop(stones_))
            if x != y:
                if x < y:
                    heapq.heappush(stones_, -(y - x))
                else:
                    heapq.heappush(stones_, -(x - y))
        

        if stones_:
            return -stones_[0]
        else:
            return 0