class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        roots = {}
        for ch in "abcdefghijklmnopqrstuvwxyz":
            roots[ch] = ch
        def get(x):
            if roots[x] != x:
                roots[x] = get(roots[x])
            return roots[x]
        def union(x, y):
            rootX = get(x)
            rootY = get(y)
            if rootX == rootY:
                return 
            
            roots[rootX] = rootY
            roots[rootY] = rootY
            roots[x] = rootY
            roots[y] = rootY
            
        for equation in equations:
            left = equation[0]
            right = equation[3]
            sign = equation[1]
            if sign == '=':
                union(left, right)
            
       
        ans = True
        for eq in equations:
            left = eq[0]
            right = eq[3]
            sign = eq[1]
            if sign == '=' and get(left) != get(right):
                ans = False
                break
            if sign == '!' and get(left) == get(right):
                ans = False
                break
        
        return ans