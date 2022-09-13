class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(s):
            num = 0
            n = len(s) 
            for i in s:
                num = num * 10 + (ord(i) - 48)
            return num
        num1 = convert(num1)
        num2 = convert(num2)
        prod = num1 * num2
        print(prod)
        ans = []
        if prod == 0:
            return "0"
        while prod != 0:
            mod = prod % 10
            ans.append(chr(ord('0') + mod))
            prod = prod // 10
        ans = ans[::-1]
        return "".join(ans)
            