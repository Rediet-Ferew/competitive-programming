class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def recurssion(n):
            if n == 0:
                return '0'
            else:
                string = ''.join('1' if b == '0' else '0' for b in recurssion(n -1)) 
                return recurssion(n - 1) + "1" + string[::-1]
            
        s = recurssion(n - 1)
        return str(s[k -1])