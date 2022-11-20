class Solution:
    def calculate(self, s: str) -> int:
        num, sign = 0, 1
        stack = [0]
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                num = 10*num + int(c)
            elif c == '+':
                stack[-1] += num * sign
                sign = 1
                num = 0
            elif c == '-':
                stack[-1] += num * sign
                sign = -1
                num = 0
            elif c == '(':
                stack.extend([sign,0])
                sign = 1
                num = 0
            elif c == ')':
                lastNum = (stack.pop() + num*sign) * stack.pop()
                stack[-1] += lastNum
                sign = 1
                num = 0
        return stack[-1]+num*sign
