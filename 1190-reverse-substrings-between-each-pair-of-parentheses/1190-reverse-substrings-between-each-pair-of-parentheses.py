class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                temp = ""
                while stack and stack[-1] != '(':
                    temp += (stack.pop())
                stack.pop()
                for t in temp:
                    stack.append(t)
            else:
                stack.append(c)
        return "".join(stack)
                    