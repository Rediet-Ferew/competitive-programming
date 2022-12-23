class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        ans = ""
        
        l = 0
        num = ord('a') - 1
        while l < n:
            
            if l < n - 2 and s[l+2] == '#':
                temp = s[l:l+2]
                ans += chr(num + int(temp))
                l += 3
                
            else:
                ans += chr(num + int(s[l]))
                l += 1
                
        return ans