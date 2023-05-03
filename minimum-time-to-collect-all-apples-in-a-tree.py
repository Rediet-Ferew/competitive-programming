class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
       
        def dfs(node, parent):
            res = 0

            for item in adj_list[node]:
                if item == parent:
                    continue
                else:
                    temp = dfs(item, node)
                    if temp or hasApple[item]:
                        res += (temp + 2)
            return res
        return dfs(0, -1)