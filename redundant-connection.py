class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(1, 1001):
            graph[i] = i
        def representative(x):
            
            if graph[x]==x:
                return x
            return representative(graph[x])

        def union(u, v):
            parent_u = representative(u)
            parent_v = representative(v)
            if parent_u == parent_v:
                return False
            graph[parent_u] = parent_v
            return True
        for u, v in edges:
            if not union(u, v):
                return (u, v)