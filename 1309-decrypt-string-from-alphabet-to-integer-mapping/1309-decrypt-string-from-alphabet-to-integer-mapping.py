class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        ans = [''] * n
        a_to_i = {}
        j_to_z = {}
        
        #map a to i to 1 to 9
#         for i, c in enumerate("abcdefghi"):
#             idx = str(i+1)
#             a_to_i[idx] = c
        
#         #map j to z to 10# to 26#
#         pos = 10
#         for i, c in enumerate("jklmnopqrstuvwxyz"):
#             t = f'{pos}#'
#             j_to_z[t] = c 
#             pos += 1
            
        l = 0
        num = ord('a') - 1
        while l < n:
            
            if l < n - 2 and s[l+2] == '#':
                temp = s[l:l+2]
                ans[l] = chr(num + int(temp))
                l += 3
                
            else:
                ans[l] = chr(num + int(s[l]))
                l += 1
                
        return "".join(ans)