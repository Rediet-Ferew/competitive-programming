class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adj_list = {}
        in_degree = [0] * n
        min_level = float("inf")
        for u, v in edges:
            if u not in adj_list:
                adj_list[u] = [v]
            else:
                adj_list[u].append(v)
            
            if v not in adj_list:
                adj_list[v] = [u]
            else:
                adj_list[v].append(u)
            in_degree[u] += 1
            in_degree[v] += 1
        q = collections.deque()
        
        for key, val in adj_list.items():
            if len(val) == 1:
                q.append(key)
            
        min_level = []
        ans = []
        
        level = 0
        while q:
            cur_len = len(q)
            temp = []
            for _ in range(cur_len):
                node = q.popleft()
                temp.append(node)
                if node in adj_list:
                    for neighbor in adj_list[node]:
                        in_degree[neighbor] -= 1
                        if in_degree[neighbor] == 1:
                            q.append(neighbor)
                            # visited.add(neighbor)
            ans.append(temp)
            level += 1
        if ans:
            return ans[-1]
        return [0]