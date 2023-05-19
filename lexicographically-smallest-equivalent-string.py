class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        #initialize a graph
        s3 = s1 + s2
        roots = {}
        for ch in s3:
            roots[ch] = ch
        
        def find(x):
            #without path compression
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]
        def union(ch1, ch2):
            par1 = find(ch1)
            par2 = find(ch2)
            
            min_val = min(ch1, ch2, par1, par2)
            roots[par1] = min_val
            roots[par2] = min_val
            roots[ch1] = min_val
            roots[ch2] = min_val
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        def find_min(ch):
            parent = ch
            while parent != roots[parent]:
                parent = roots[parent]
            return parent
        
        t = ""
        for ch in baseStr:
            if ch not in roots:
                t += ch
            else:
                t += find_min(ch)
        return t