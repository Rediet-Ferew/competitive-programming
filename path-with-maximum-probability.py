class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for idx, nodes in enumerate(edges):
            u, v = nodes
            graph[u].append([v, succProb[idx]])
            graph[v].append([u, succProb[idx]])
        heap = []
        heapq.heappush(heap, [-1.00000, start_node])
        visited = [float("-inf")] * n
        seen = set()
        visited[start_node] = 1.00000
        while heap:
            w, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            visited[node] = -1 * w
            for neigh, neigh_w in graph[node]:
                dis = -1 * w * neigh_w
                if dis > visited[neigh]:
                    visited[neigh] = dis
                    heapq.heappush(heap, [-1 * dis, neigh])
        if visited[end_node] == float("-inf"):
            return round(0, 5)
        else:
            return round(visited[end_node], 5)