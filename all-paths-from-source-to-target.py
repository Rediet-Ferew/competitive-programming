class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #create adjancency list
        adj_list = defaultdict(list)

        outer = len(graph)
        # print(outer)
        final = 0

        for i in range(outer):
            if i == outer - 1:
                final = i
            adj_list[i].extend(graph[i])
        
        # print(adj_list)
        visited = set()
        res = []
        def dfs(node, arr):
            if node == final:
                res.append(arr.copy())
                return 
            # if node in visited:
            #     return
            if node not in visited:
                arr.append(node)
                visited.add(node)
            for j in range(len(adj_list[node])):
                if adj_list[node][j] not in visited:
                    arr.append(adj_list[node][j])
                    visited.add(adj_list[node][j])
                    dfs(adj_list[node][j], arr)
                    # print(arr)
                    arr.pop()
                    visited.remove(adj_list[node][j])
        dfs(0, [])
        return res
        # return []