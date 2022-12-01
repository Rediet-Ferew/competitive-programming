class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        h = n//2
        vowels_a = 0
        vowels_b = 0
        a = s[:h]
        b = s[h:]
        for ch in a:
            if ch in 'AEIOUaeiou':
                vowels_a += 1
        for c in b:
            if c in 'AEIOUaeiou':
                vowels_b += 1
        return vowels_a == vowels_b