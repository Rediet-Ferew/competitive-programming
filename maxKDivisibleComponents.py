class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if not edges:
            return int(values[0] % k == 0)
        graph = {}
        
        parents = {0: -1}
        leafs = collections.deque()
        cnt = 0
        count = {}
        for u, v in edges:
            
            if u in graph:
                
                graph[u].append(v)
            else:
                graph[u] = [v]
                
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]
        # print(graph)
        visited = set()
        seen = set()
        def dfs(parent, node):
            
            if node in visited:
                return
            visited.add(node)
            parents[node] = parent
            count[parent] = 1 + count.get(parent, 0)
            if node in graph:
                for neigh in graph[node]:
                    
                    dfs(node, neigh)
    
            if len(graph[node]) == 1 and node != 0:
                leafs.append(node)
                # seen.add(node)
           
            
        dfs(-1, 0)
        # print(leafs)
        # print(parents)
        # print(count)
        while leafs:
            curLen = len(leafs)
            for _ in range(curLen):
                node = leafs.popleft()
                p = parents[node]
                count[p] -= 1
              
                if values[node] % k == 0:
                    cnt += 1
    
                else:
                    values[p] += values[node]
                if p >= 0 and count[p] == 0:
                        leafs.append(p)
            # print(leafs)
        return cnt

                




