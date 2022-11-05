class Solution:
    def calculate(self, s: str) -> int:
        sign = '+'
        num = 0
        stack = []
        for i, n in enumerate(s):
            if n.isnumeric():
                num = num * 10 + int(n)
            if n in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    res = stack.pop() * num
                    stack.append(res)
                elif sign == '/':
                    res = int(stack.pop() / num)
                    stack.append(res)
                sign = n
                num = 0
        
        return sum(stack)