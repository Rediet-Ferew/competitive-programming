class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = []
        numsFreq = Counter(nums)
        print(numsFreq)
        heap = [(-val, key) for key, val in numsFreq.items()]
        heapq.heapify(heap)
        for i in range(k):
            final.append(heapq.heappop(heap)[1])
        return final
       