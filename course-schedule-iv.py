class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        def dfs(u, v):
            nonlocal flag
            if u in visited:
                return 
            visited.add(u)
            if u == v:
                flag = True
                return
            
            for child in adj_list[u]:
                dfs(child, v)

        adj_list = collections.defaultdict(list)

        for pre in prerequisites:
            adj_list[pre[0]].append(pre[1])
        
        ans = [False] * len(queries)

        for i in range(len(queries)):
            u, v = queries[i]

            flag = False
            visited = set()
            dfs(u, v)
            ans[i] = flag
        return ans