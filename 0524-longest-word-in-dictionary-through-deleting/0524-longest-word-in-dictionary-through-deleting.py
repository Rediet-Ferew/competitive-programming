class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isFound(string):
            l = 0
            for c in s:
                if c == string[l]:
                    l += 1
                if l == len(string):
                    return True
            return l == len(string)
        dictionary.sort()
        dictionary.sort(key=len, reverse=True)
        for string in dictionary:
            if isFound(string):
                return string
        return ""