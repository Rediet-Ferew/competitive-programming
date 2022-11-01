class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        n = len(arr)
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        length = n
        counter = 0
        while length > n // 2:
            val, key = heapq.heappop(heap)
            length -= (-1*val)
            counter += 1
        return counter
        
        
            