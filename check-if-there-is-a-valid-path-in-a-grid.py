class DisjointSet:
    def __init__(self, n, m):
        self.roots = {}
        for r in range(n):
            for c in range(m):
                self.roots[(r, c)] = (r, c)
        
        self.rank = defaultdict(int)
    def get(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.get(self.roots[x])
        return self.roots[x]
    def union(self, x, y):
        rootX = self.get(x)
        rootY = self.get(y)
        if rootX == rootY:
            return 
        if self.rank[rootX] == self.rank[rootY]:
            self.roots[rootX] = rootY
            self.rank[rootX] += 1
        if self.rank[rootX] > self.rank[rootY]:
            self.roots[rootX] = rootY
        else:
            self.roots[rootY] = rootX
            
    def isConnected(self, u, v):
        return self.get(u) == self.get(v)
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        rowLen = len(grid)
        colLen = len(grid[0])
        ds = DisjointSet(rowLen, colLen)
       
        def isValid(r, c):
            return r >= 0 and r < rowLen and c >= 0 and c < colLen
        directions = {"l": (0, -1), "r": (0, 1), "u": (-1, 0), "d": (1, 0)}
        
        validConnections = {
            "l": set({(1,4),(1,6),(3,1),(3,4),(3,6),(5,6),(5,4),(5,1),(1,2)}),
            "r": set({(1,3),(1,5),(4,1),(4,3),(4,5),(6,3),(6,4),(6,1),(1,1)}),
            "u": set({(2,3),(2,4),(5,3),(5,4),(5,2),(6,3),(6,4),(6,2),(2,2)}),
            "d": set({(2,5),(2,6),(3,5),(3,6),(3,2),(4,5),(4,6),(4,2),(2,2)})
        }
        
        for r in range(rowLen):
            for c in range(colLen):
                for key, val in directions.items():
                    nr, nc = r + val[0], c + val[1]
                    
                    if isValid(nr, nc):
                        t = tuple((grid[r][c], grid[nr][nc]))
                        # print(t)
                        if t in validConnections[key]:
                            ds.union((r, c), (nr, nc))
        
        return ds.isConnected((0, 0), (rowLen - 1, colLen - 1))