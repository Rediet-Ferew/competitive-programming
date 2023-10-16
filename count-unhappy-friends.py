class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        take index as weight, if the pair is at index 0 -> continue
        if not find befores in the graph

        """
        
        rank = [[0 for i in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                num = preferences[i][j]
                rank[i][num] = j 
        print(rank)
        graph = []
        for u, v in pairs:
            graph.append([v, u])
        pairs = pairs + graph

        print(pairs)
        cnt = 0
        #     if u in graph:
        #         graph[u].append(v)
        #     else:
        #         graph[u] = [v]
        #     if v in graph:
        #         graph[v].append(u)
        #     else:
        #         graph[v] = [u]
           
        for i in range(n):
            x, y = pairs[i]
            for j in range(n):
                u, v = pairs[j]
                if i != j:
                    if rank[x][y] > rank[x][u] and rank[u][v] > rank[u][x]:
                        cnt += 1
                        break
        return cnt