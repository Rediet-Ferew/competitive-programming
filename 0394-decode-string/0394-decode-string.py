class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            if s[i] != ']':
                result.append(s[i])
            else:
                string = ""
                while result[-1] != '[':
                    string = result.pop() + string
                result.pop()
                sub = ""
                while result and result[-1].isdigit():
                    sub = result.pop() + sub
                result.append(int(sub) * string)
        return "".join(result)
                
                    
                    
            

        
                