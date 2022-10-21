class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gptr = 0
        sptr = 0
        children = 0
        while gptr < len(g) and sptr < len(s):
            if s[sptr] >= g[gptr]:
                children += 1
                gptr += 1
                sptr += 1
            else:
                sptr += 1
        return children