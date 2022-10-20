class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s) 
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] not in "aeiouAEIOU":
                left += 1
            if s[right] not in "aeiouAEIOU":
                right -= 1
            if s[left] in "aeiouAEIOU" and s[right] in "aeiouAEIOU":
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
        
            