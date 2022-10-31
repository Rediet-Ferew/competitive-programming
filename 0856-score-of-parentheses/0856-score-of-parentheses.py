class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
       
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)
            else:
                if stack[-1] == 0:
                    stack.pop()
                    stack.append(1)
                else:
                    count = 0
                    while stack and stack[-1] != 0:
                        count += stack[-1]
                        stack.pop()
                    stack.pop()
                    stack.append(2 * count)
        res = 0        
        while stack:
            res +=stack[-1]
            stack.pop()
        return res