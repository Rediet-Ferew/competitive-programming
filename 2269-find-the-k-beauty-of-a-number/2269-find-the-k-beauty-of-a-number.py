class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        s = str(num)
        l = 0
        r = k - 1
        counter = 0
        while r < len(s):
            temp = int(s[l : r+1])
            if temp == 0:
                l += 1
                r += 1
                continue
            if num % temp == 0:
                counter += 1
            l += 1
            r += 1
        return counter
        
        