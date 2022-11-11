class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """
        total = 2 + 2 + 7
        [17,12,10,2,7,2,11,20,8]
                    lr
        lheap = [10,12,17]
        rheap = [8,11,20]
        
        """
        total = 0
        n = len(costs)
        # if k >= n:
        #     return sum(costs)
        if 2*candidates > n:
            return sum(sorted(costs)[:k])
        l = candidates - 1
        r = n - candidates
        lheap = costs[:min(l+1,n)]+[float("inf")]
        rbound = max(0,r,(l+1))
        rheap =costs[rbound:]+[float("inf")]
        heapq.heapify(lheap)
        heapq.heapify(rheap)
        for i in range(k):
            if lheap[0] <= rheap[0]:
                total += heapq.heappop(lheap)
                l += 1
                if l < r and l < n:
                    heapq.heappush(lheap, costs[l])
            else:
                total += heapq.heappop(rheap)
                r -= 1
                if l < r and r >= 0:
                    heapq.heappush(rheap,costs[r])
        return total
        