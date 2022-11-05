class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {'{': '}', '[':']', '(':')'}
        # if len(s) % 2 != 0:
        #     return False
        for brace in s:
            if brace in braces:
                stack.append(brace)
            elif brace not in braces:
                if not stack:
                    return False
                elif stack and braces[stack[-1]] != brace:
                    return False
                elif stack and braces[stack[-1]] == brace:
                    stack.pop()
        return len(stack) == 0