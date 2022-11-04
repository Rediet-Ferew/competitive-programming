class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        def check(s1,s2):
            l=0
            r=n-1
            while l<=r and s1[l]==s2[r]:
                l+=1
                r-=1
            
            if l>r or s1[l:r+1]==s1[l:r+1][::-1] or s2[l:r+1]==s2[l:r+1][::-1]:
                return True
            return False
        return check(a,b) or check(b,a)
                
                