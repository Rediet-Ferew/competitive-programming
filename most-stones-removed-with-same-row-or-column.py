class DisjointSet:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]
    def get(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.get(self.roots[x])
        return self.roots[x]
    def union(self, x, y):
        rootX = self.get(x)
        rootY = self.get(y)
        if rootX == rootY:
            return 
        if self.size[rootX] == self.size[rootY]:
            self.roots[rootX] = rootY
            
            self.size[rootY] += self.size[rootX]

        elif self.size[rootX] > self.size[rootY]:
            self.roots[rootY] = rootX
            self.size[rootX] += self.size[rootY]
          
        else:
            self.roots[rootX] = rootY
            self.size[rootY] += self.size[rootX]
      
            
    def isConnected(self, u, v):
        return self.get(u) == self.get(v)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        disjoint = DisjointSet(n)
        for r in range(n):
            for c in range(n):
                if stones[r][0] == stones[c][0] or stones[r][1] == stones[c][1]:
                    disjoint.union(r, c)
        ans = n
        for i in range(n):
            if disjoint.get(i) == i:
                ans -= 1
        return ans