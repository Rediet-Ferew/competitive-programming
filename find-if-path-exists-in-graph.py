class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {}
        for i in range(n):
            graph[i] = i
        def representative(x):
            
            if graph[x]==x:
                return x
            return representative(graph[x])

        def union(u, v):
            parent_u = representative(u)
            parent_v = representative(v)
            if parent_u == parent_v:
                return
            graph[parent_u] = parent_v
        
        for u, v in edges:
            union(u, v)
        
        print(graph)
        return representative(source) == representative(destination)