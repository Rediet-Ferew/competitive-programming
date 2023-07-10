class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj_list = defaultdict(list)
        for u in range(n):
            x1, y1 = points[u]
            for v in range(u + 1, n):
                x2, y2 = points[v]
                d = abs(x2 - x1) + abs(y2 - y1)
                adj_list[u].append([d, v])
                adj_list[v].append([d, u])
        
        ans = 0
        visited = set()
        min_heap = [[0, 0]]
        while len(visited) < n:
            cost, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            ans += cost
            visited.add(point)
            for cost_n, neighbor in adj_list[point]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, [cost_n, neighbor])
        return ans