class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        ans = ['']*n
        i = 0
        while i < n:
            if command[i] == 'G':
                ans[i] = 'G'
                i += 1
            elif i < n - 1 and command[i] == '(':
                if command[i+1] == ')':
                    ans[i] = 'o'
                    i += 2
                elif command[i+1] == 'a':
                    ans[i] = 'al'
                    i += 4
        return "".join(ans)