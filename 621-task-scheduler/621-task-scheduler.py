class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        Heap = []
        for occ in count.values():
            Heap.append(-(occ))
        heapq.heapify(Heap)
        time = 0
        que = deque()
        while Heap or que:
            time += 1
            if Heap:
                occ = 1 + heapq.heappop(Heap)
                if occ:
                    que.append([occ, time + n])
            if que and que[0][1] == time:
                heapq.heappush(Heap, que.popleft()[0])
        return time
                
                
            