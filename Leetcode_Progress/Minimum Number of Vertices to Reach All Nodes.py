class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sources = set()
        sinks = set()
        for i in range(len(edges)):
            s, d = edges[i]
            sources.add(s)
            sinks.add(d)
        src = sources.difference(sinks)
        return src
