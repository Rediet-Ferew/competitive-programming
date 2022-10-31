class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        indices = {}
        res = []
        for idx, ch in enumerate(s):
            indices[ch] = idx
        for i, c in enumerate(s):
            if c not in res:
                while res and i < indices[res[-1]] and c < res[-1]:
                    res.pop()
                res.append(c)
        return "".join(res)
                    
                    
            