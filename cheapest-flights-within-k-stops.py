class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])
        
        # print(graph)
        heap = []
        visited = [float("inf")] * n
        heapq.heappush(heap, [0, 0, src])
        visited[src] = 0
        seen = set()
        temp =[]
        while heap:
            cnt, w, node = heapq.heappop(heap)
            
            for neigh, neigh_w in graph[node]:
                dist = neigh_w + w
                
                if dist < visited[neigh] and cnt <= k:
                    visited[neigh] = dist
                    heapq.heappush(heap, [cnt + 1, dist, neigh])
            
        if visited[dst] == float("inf"):
            return -1
        return visited[dst]