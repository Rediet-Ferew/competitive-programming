class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split('/')
        # print(p)
        stack = []
        for i in range(len(p)):
            if stack and p[i] == '..':
                stack.pop()
            if p[i] == '.':
                continue
            if p[i] != '..' and p[i] != '.' and p[i] != '':
                stack.append(p[i])
        result = "/"
        result += "/".join(stack)
        return result
                
        