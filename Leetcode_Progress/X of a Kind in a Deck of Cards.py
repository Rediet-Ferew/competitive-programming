class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def check(a, b):
            if b == 0:
                return a
            else:
                return check(b, a % b)
        cnt = Counter(deck)
        # print(cnt)
        ls = list(cnt.values())
        ls.sort()
        hcf = ls[0]
            
        for j in range(len(ls)):
            hcf = check(hcf, ls[j])
        if hcf > 1:
            return True
        return False
       
        
