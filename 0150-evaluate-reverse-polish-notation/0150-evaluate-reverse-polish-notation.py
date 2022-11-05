class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = 0
        for c in tokens:
            if c not in "+*/-":
                stack.append(int(c))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if c == '+':
                    answer = int(num2 + num1)
                elif c == '-':
                    answer = int(num2 - num1)
                elif c == '*':
                    answer = int(num2 * num1)
                elif c == '/':
                    answer = int(num2 / num1)
                stack.append(answer)
        return stack[0]
