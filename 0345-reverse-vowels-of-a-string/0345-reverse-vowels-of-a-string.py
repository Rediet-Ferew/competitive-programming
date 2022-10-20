class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1:
            return s
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
        # vowels = {}
        # s = list(s)
        # for i in range(len(s)):
        #     if s[i] in "aeiouAEIOU":
        #         vowels[i] = s[i]
        # keys = list(vowels.keys())
        # while len(keys) > 1:
        #     s[keys[0]], s[keys[-1]] = s[keys[-1]], s[keys[0]]
        #     del keys[0]
        #     keys.pop()
        # return "".join(s)
            