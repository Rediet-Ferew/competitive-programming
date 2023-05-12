class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        #add it to min heap
        heapq.heappush(self.min_heap, num)
        if self.min_heap and self.max_heap and (-1*self.max_heap[0]) > (self.min_heap[0]):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1*val)
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1*val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)


    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            l = -1*self.max_heap[0]
            r = self.min_heap[0]
            return (l + r) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -1*self.max_heap[0]
        else:
            return self.min_heap[0]
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()