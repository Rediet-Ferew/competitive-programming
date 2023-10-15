class Solution:
    def countVowels(self, word: str) -> int:
        counter = 0
        n = len(word)
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(n):
            if word[i] in vowels:
                counter += (i + 1) * (n - i)
        return counter