class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n + 1)
        letters = list(s)
        for i in range(len(shifts)):
            
            start, end, dirn = shifts[i]
            
            if dirn == 0:
                prefix[start] += -1
                prefix[end + 1] += 1
            else:
                prefix[start] += 1
                prefix[end + 1] -= 1
                
        for j in range(1, n + 1):
            prefix[j] += prefix[j - 1]
            
        for k in range(n):
            shift = prefix[k]
            shift = shift % 26
            ch_ord = ord(letters[k])
            
                
            sh_ord = ch_ord + (shift)
            
            if sh_ord < 97:
                n_sh_ord = 122 - ((97 - sh_ord) - 1)
                letters[k] = chr(n_sh_ord)
            elif sh_ord > 122:
                n_sh_ord = 97 + ((sh_ord - 122) - 1)
                letters[k] = chr(n_sh_ord)
            else:
                letters[k] = chr(sh_ord)
        
        return "".join(letters)