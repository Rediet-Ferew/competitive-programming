class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {}
        s = list(s)
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                vowels[i] = s[i]
        keys = list(vowels.keys())
        while len(keys) > 1:
            s[keys[0]], s[keys[-1]] = s[keys[-1]], s[keys[0]]
            del keys[0]
            keys.pop()
        return "".join(s)
            