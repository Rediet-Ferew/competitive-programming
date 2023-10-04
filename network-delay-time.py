class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])
        print(graph)
        heap = []
        seen = set()
        
        visited = [float("inf")] * (n + 1)
        visited[k] = 0
        heapq.heappush(heap, [0, k])
        while heap:
            weight, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            
            # visited[node] = weight
            
            for neigh, neigh_w in graph[node]:
                w = neigh_w + weight
                print(w, neigh)
                if w < visited[neigh]:
                    visited[neigh] = w
                    heapq.heappush(heap, [w, neigh])
        print(visited)
        visited[0] = 0
        if float("inf") in visited:
            return -1
        
        return max(visited)