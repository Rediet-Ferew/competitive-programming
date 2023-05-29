class DisjointSet:
    def __init__(self, n):
        
        self.roots = {}
        for i in range(n):
            self.roots[i] = i
        self.rank = [0 for i in range(n)]
    def get(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.get(self.roots[x])
        return self.roots[x]
    def union(self, x, y):
        #indices of letters
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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    
        n = len(s)
        slist = list(s)
        ds = DisjointSet(n)
        for u, v in pairs:
           
            ds.union(v, u)

        m = defaultdict(list)
        m_ = defaultdict(list)
        for i in range(n):
            pr = ds.get(i)
            m[pr].append(i)
        for k, v in m.items():
            v.sort()
            temp = sorted(v, key= lambda x:s[x])
            m_[k].extend(temp)
        for key, val in m.items():
            l1 = m[key]
            l2 = m_[key]
            for p1, p2 in zip(l1, l2):
                slist[p1] = s[p2]
                 
        return "".join(slist)