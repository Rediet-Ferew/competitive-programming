class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack = list(haystack)
        needle = list(needle)
        n = len(needle)
        h = len(haystack)
        idx = -1
        if needle == haystack:
            return 0
        for i in range(h - n + 1):
            if needle == haystack[i : i + n]:
                idx = i
                break
        return idx