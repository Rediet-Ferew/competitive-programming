class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for point in points:
            dis = (point[0] ** 2) + (point[1] ** 2)
            minHeap.append([dis, point[0], point[1]])
        heapq.heapify(minHeap)
        while k > 0:
            dis, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res
            
        