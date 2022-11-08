class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and chr(ord(stack[-1]) - 32) == c:
                if stack and chr(ord(stack[-1]) - 32) == c:
                    stack.pop()
            elif stack and chr(ord(stack[-1]) + 32) == c:
                if stack and chr(ord(stack[-1]) + 32) == c:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)