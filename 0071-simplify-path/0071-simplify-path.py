class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        stack = []
        
        right = 0
        while right < n:
            if path[right] == '/':
                i = right
                while i < n and path[i] == '/':
                    i += 1
                right = i
            elif path[right] != '/':
                j = right
                temp = ""
                while j < n and path[j] != '/':
                    temp += path[j]
                    j += 1
                if temp == '..':
                    if stack:
                        stack.pop()
                elif temp != '.':
                    stack.append(temp)
                        
                right = j
                
        reduced_path = '/'
        reduced_path += "/".join(stack)
        return reduced_path