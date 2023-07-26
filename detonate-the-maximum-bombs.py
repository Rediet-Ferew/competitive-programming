class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = {}
        n = len(bombs)
        
        for i in range(n):
            x, y, r = bombs[i]
            graph[i] = []
            
            for j in range(n):
                x2, y2, r2 = bombs[j]
                if i == j:
                    continue
                if (x2 - x) ** 2 + (y - y2) ** 2 <= r**2:
                    graph[i].append(j)
        print(graph)
        def dfs(node):
            nonlocal cnt
            if node in visited:
                return 0
            cnt += 1
            visited.add(node)
            
            for v in graph[node]:
                if v not in visited:
                    # visited.add(v)
                    # cnt += 1
                    dfs(v)
            
            return cnt
        max_bombs = 0
        for key, val in graph.items():
            visited = set()
            cnt = 0
            dfs(key)
            # print(cnt)
            max_bombs = max(max_bombs, cnt)
        return max_bombs