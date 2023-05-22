class DisjointSet:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.min_edges = [inf for _ in range(n)]
    def get(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.get(self.roots[x])
        return self.roots[x]
    def union(self, x, y, weight):
        rootX = self.get(x)
        rootY = self.get(y)
        if rootX == rootY:
            self.min_edges[rootX] = min(weight, self.min_edges[rootX], self.min_edges[rootY])
            return 
        if self.rank[rootX] == self.rank[rootY]:
            self.roots[rootX] = rootY
            self.min_edges[rootY] = min(weight, self.min_edges[rootX], self.min_edges[rootY])
            self.rank[rootX] += 1
        elif self.rank[rootX] > self.rank[rootY]:
            self.roots[rootY] = rootX
            self.min_edges[rootX] = min(weight, self.min_edges[rootX], self.min_edges[rootY])
        else:
            self.roots[rootX] = rootY
            self.min_edges[rootY] = min(weight, self.min_edges[rootX], self.min_edges[rootY])
            
    def isConnected(self, u, v):
        return self.get(u) == self.get(v)
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        disjoint = DisjointSet(n)
        for u, v, d in roads:
            disjoint.union(u - 1, v - 1, d)
        
        parent = disjoint.get(n - 1)
        # print(parent)
        return disjoint.min_edges[parent]
        
        # return 0