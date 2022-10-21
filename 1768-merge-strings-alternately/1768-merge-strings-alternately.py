class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        first = 0
        second = 0
        while first < len(word1) and second < len(word2):
            result += word1[first]
            result += word2[second]
            first += 1
            second += 1
        while first < len(word1):
            result += word1[first]
            first += 1
        while second < len(word2):
            result += word2[second]
            second += 1
        return result

            