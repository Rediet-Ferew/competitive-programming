class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        # sList = list(s)
        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            else:
                word = ""
                while stack and stack[-1] != '(':
                    word += stack.pop()
                stack.pop()
                stack.extend(list(word))
        return ''.join(stack)
                
                
            
                
        # sList = list(s)
        # print(sList)