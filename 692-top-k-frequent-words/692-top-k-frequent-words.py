class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        final = []
        wordsFreq = Counter(words)
        print(wordsFreq)
        heap = [(-val, key) for key, val in wordsFreq.items()]
        heapq.heapify(heap)
        for i in range(k):
            final.append(heapq.heappop(heap)[1])
        return final