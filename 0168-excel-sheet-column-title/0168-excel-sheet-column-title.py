class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num = columnNumber
        title = ""
        while num > 0:
            num -= 1
            mod = num % 26
            
            title += (chr(ord('A') + mod)) 
            
            num = num // 26
       
        return str(title[::-1])
    
            