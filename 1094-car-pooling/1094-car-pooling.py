class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        heap = []
        currentPass = 0
        for trip in trips:
            passengers, start, end = trip
            while heap and heap[0][0] <= start:
                currentPass -= heap[0][1]
                heapq.heappop(heap)
            currentPass += passengers
            if currentPass > capacity:
                return False
            heapq.heappush(heap, [end, passengers])
        return True
        