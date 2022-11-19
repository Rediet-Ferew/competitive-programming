class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s.strip()
        n = len(s)
        final = 0
        for i in range(n-1, -1,-1):
            if s[i] != ' ':
                final+=1
            else:
                break
        return final