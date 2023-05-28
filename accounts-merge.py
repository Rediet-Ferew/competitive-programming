class DisjointSet:
    def __init__(self, graphs):
        self.roots = graphs
        self.rank = {}
        for k, v in self.roots.items():
            self.rank[k] = 0
    def get(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.get(self.roots[x])
        return self.roots[x]
    def union(self, x, y):
        rootX = self.get(x)
        rootY = self.get(y)
        # if rootX == rootY:
        #     return 
        # if self.rank[rootX] == self.rank[rootY]:
        #     self.roots[rootX] = rootY
        #     self.rank[rootX] += 1
        # if self.rank[rootX] > self.rank[rootY]:
        #     self.roots[rootX] = rootY
        # else:
        #     self.roots[rootY] = rootX
        self.roots[rootX] = rootX
        self.roots[rootY] = rootX
        self.roots[x] = rootX
        self.roots[y] = rootX
    def isConnected(self, u, v):
        return self.get(u) == self.get(v)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #email map
        parent_store = {}
        graphs = {}
        for r in range(len(accounts)):
            par = accounts[r][0]
            for c in range(1, len(accounts[r])):
                parent_store[accounts[r][c]] = par
                graphs[accounts[r][c]] = accounts[r][c]
        ds = DisjointSet(graphs)
        for i in range(len(accounts)):
            
            for j in range(1, len(accounts[i]) - 1):
                
                ds.union(accounts[i][j], accounts[i][j + 1])
        
        ans = collections.defaultdict(list)
        for k, v in ds.roots.items():
            pr = ds.get(k)
            ans[pr].append(k)
        res = []
        for key, val in ans.items():
            temp = [parent_store[key]]
            temp.extend(sorted(val))
            res.append(temp)
        return res