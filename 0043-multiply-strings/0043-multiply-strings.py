class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert_to_int(num):
            ans = 0
            for n in num:
                ans = (ans * 10) + (ord(n) - 48)
            return ans
        if num1 == '0' or num2 == '0':
            return '0'
        n1 = convert_to_int(num1)
        n2 = convert_to_int(num2)
        mul = n1 * n2
        res = ""
        while mul > 0:
            mod = mul % 10
            c = chr(ord('0') + mod)
            res = c + res
            mul = mul//10
        return res