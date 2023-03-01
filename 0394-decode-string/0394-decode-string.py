class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        
        
        for right in range(n):
            
            if s[right] != ']':
                
                stack.append(s[right])
                
                
            else:
                
                temp = ""
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                # print(temp)
                
                stack.pop()
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                # print(num)
                # num = int(num)
                
                stack.append(int(num) * temp)
        while stack and stack[-1].isdigit():
            stack.pop()
        # print(stack)
        return "".join(stack)