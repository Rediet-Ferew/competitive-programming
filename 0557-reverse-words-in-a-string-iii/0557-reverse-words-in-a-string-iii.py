class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        s.append(' ')
        l = 0;
        for r in range(len(s)):
            if s[r] == ' ':
                s[l:r] = s[l:r][::-1]
                l = r + 1
        return "".join(s[:-1])