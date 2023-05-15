class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = {}
        res = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            if u not in adj_list:
                adj_list[u] = [v]
                
            else:
                adj_list[u].append(v)
            
            in_degree[v] += 1
        q = collections.deque()
        for i in range(n):
            if in_degree[i] == 0:
                
                q.append(i)
        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                p = q.popleft()
                if p in adj_list:
                    for neighbor in adj_list[p]:
                        if in_degree[neighbor] != 0:
                            prev = set(res[p])
                            ng = set(res[neighbor])
                            ng.add(p)
                            prev = prev.union(ng)

                            res[neighbor]=list(prev)
                            in_degree[neighbor] -= 1
                        if in_degree[neighbor] == 0:
                            q.append(neighbor)

        ans = [[] for _ in range(n)]
        for key, val in res.items():
            ans[key] = sorted(val)
        return ans

        
                




        # print(adj_list)
        # print(in_graph)
        # print(in_degree)