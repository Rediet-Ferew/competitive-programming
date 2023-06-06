class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(target)
        
        parent = {i: i for i in range(n)}
        rank = {i: 1 for i in range(n)}
        
        def get(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rootX = get(x)
            rootY = get(y)
            if rootX == rootY:
                return 0
            if rank[rootX] < rank[rootY]:
                rootX, rootY = rootY, rootX
            parent[rootY] = rootX
            rank[rootX] += rank[rootY]
            return 1
        
        for i, j in allowedSwaps:
            union(i, j)
        
        dis = defaultdict(list)
        
        for i in range(n):
            dis[get(i)].append(i)
        
        total = 0
        
        for x in dis.values():
            s = Counter()
            t = Counter()
            
            for i in x:
                s[source[i]] += 1
                t[target[i]] += 1
        
            final = s & t
            total += sum(final.values())
    
        return len(source) - total