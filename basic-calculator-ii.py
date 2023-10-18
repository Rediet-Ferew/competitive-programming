class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        n = len(s)
        # print(s[-1])
        stack = []
        sign = ""
        i = 0
        while i < n:
            if not s[i].isdigit():
                sign = s[i]
                i += 1
            
            elif s[i].isdigit():
                num = ""
                j = i
                while j < n and s[j].isdigit():
                    num += s[j]
                    j += 1
                i = j
                if not sign:
                    stack.append(int(num))
                elif sign == "+":
                    stack.append(int(num))
                elif sign == "-":
                    stack.append(-1 * int(num))
                elif sign == "*":
                    num1 = stack.pop()
                    num2 = int(num)
                    stack.append(num1 * num2)
                elif sign == "/":
                    num1 = stack.pop()
                    num2 = int(num)
                    # print(int(num1 / num2))
                    stack.append(int(num1 / num2))
        
        return sum(stack)