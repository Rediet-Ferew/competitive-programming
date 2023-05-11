class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        heap = []
        for i in range(rowLen):
            for j in range(colLen):
                heapq.heappush(heap, -matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        # print(heap)
        return -heapq.heappop(heap)