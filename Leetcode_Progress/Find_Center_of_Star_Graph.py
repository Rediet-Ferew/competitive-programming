class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append(v)
            graph[v].append(u)
        for key, val in graph.items():
            if len(val) == len(set(val)) and (len(val) == len(graph) - 1):
                return key
