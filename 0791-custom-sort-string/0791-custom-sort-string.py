class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sList = sorted(s)
        res = [""] * len(s)
        indices = {}
        for idx, ch in enumerate(order):
            indices[ch] = idx
        for i in range(len(sList)):
            if sList[i] in indices:
                idx = indices[sList[i]]
                if res[idx] ==  '':
                    res[idx] = sList[i]
                else:
                    res[idx] += sList[i]
        for j in range(len(sList)):
            if (sList[j] not in indices):
                res.append(sList[j])
        return ("".join(res))
        
        