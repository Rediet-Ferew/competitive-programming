class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        ans = [''] * n
        a_to_i = {}
        j_to_z = {}
        for i, c in enumerate("abcdefghi"):
            idx = str(i+1)
            a_to_i[idx] = c
        pos = 10
        for i, c in enumerate("jklmnopqrstuvwxyz"):
            t = f'{pos}#'
            j_to_z[t] = c 
            pos += 1
        l = 0
        while l < n:
            if l < n - 2 and s[l+2] == '#':
                temp = s[l:l+3]
                ans[l] = j_to_z[temp]
                l += 3
            else:
                ans[l] = a_to_i[s[l]]
                l += 1
        return "".join(ans)