class Solution:
    def validPalindrome(self, s: str) -> bool:
        # s = list(s)
        l = 0
        r = len(s) - 1
        # if s == s[::-1]:
        #     return True
        while l < r:
            if s[l] != s[r]:
                R = s[l + 1:r + 1]
                L = s[l:r]
                return (L == L[::-1] or R == R[::-1])    
            l += 1
            r -= 1
        return True
        
                