class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        visited= set()
        def dfs(node, visited, adj_list):
            
            if node in visited:
                return
            else:
                visited.add(node)
                for k in adj_list[node]:
                    dfs(k, visited, adj_list)

        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if isConnected[r][c] == 1:
                    adj_list[r + 1].append(c + 1)
        # print(adj_list)
        cnt = 0
        for i in range(1, len(isConnected) + 1):
            if i not in visited:
                dfs(i, visited, adj_list)
                cnt += 1
        return cnt