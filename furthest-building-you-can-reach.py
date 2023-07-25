class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap_ = []
        path = 0
        for i in range(1, len(heights)):

            diff = heights[i] - heights[i - 1]
            if diff > 0:
                heapq.heappush(heap_, diff)
            
            if heap_ and len(heap_) > ladders:
                val = heapq.heappop(heap_)
                bricks -= val
            
            if bricks < 0:
                return i - 1
        if bricks >= 0:
            return len(heights) - 1
        else:
            return -1