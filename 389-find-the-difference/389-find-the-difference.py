class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        s = list(s)
        for c in s:
            if c in t:
                t.remove(c)
        return str(t[0])
        
        