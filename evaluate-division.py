class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(queries)
        graph = {}
        for idx, nums in enumerate(equations):
            num, den = nums
            if num in graph:
                graph[num].append([den, values[idx]])
            else:
                graph[num] = [[den, values[idx]]]
            if den in graph:
                graph[den].append([num, 1 / values[idx]])
            else:
                graph[den] = [[num, 1 / values[idx]]]
            # format(number, ".5f")
        #djikstra
        ans = []
        for i in range(n):
            src, des = queries[i]
            if src not in graph or des not in graph:
                ans.append(-1.00000)
                continue
            heap = []
            heapq.heappush(heap, [1.00000, src])
            visited = {}
            for key, val in graph.items():
                visited[key] = float("inf")
            visited[src] = 1.00000
            seen = set()
            while heap:
                w, node = heapq.heappop(heap)
                if node in seen:
                    continue
                seen.add(node)
                visited[node] = w
                for neigh, neigh_w in graph[node]:
                    dis = w * neigh_w
                    if dis < visited[neigh]:
                        visited[neigh] = dis
                        heapq.heappush(heap, [dis, neigh])
            print(visited)
            if visited[des] == float("inf"):
                ans.append(-1.00000)
            else:
                ans.append(round(visited[des], 5))
        return ans