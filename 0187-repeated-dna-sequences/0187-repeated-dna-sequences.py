class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        occurrence = {}
        l = 0
        r = 9
        while r < len(s):
            dna = s[l:r+1]
            occurrence[dna] = 1 + occurrence.get(dna, 0)
            r += 1
            l += 1
        res = []
        for dna in occurrence:
            if occurrence[dna] > 1:
                res.append(dna)
        return res
        