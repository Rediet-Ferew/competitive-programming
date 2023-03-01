class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        last_idx = {}
        for idx, letter in enumerate(s):
            last_idx[letter] = idx
        
        stack = []
        for i in range(n):
            ch = s[i]
            
            if ch not in stack:
                
                while stack and stack[-1] > ch and last_idx[stack[-1]] > i:
                    stack.pop()
            
                stack.append(ch)
            
        return "".join(stack)
                    
                    
            