class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        sCount, pCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        
        res = []
        if sCount == pCount:
            res.append(0)
        l = 0
        r = len(p)
        while r < len(s):
            sCount[s[l]] -= 1
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
            r += 1
        return res
        