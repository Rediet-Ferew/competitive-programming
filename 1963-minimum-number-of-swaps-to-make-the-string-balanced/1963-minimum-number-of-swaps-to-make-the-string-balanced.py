class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        n = len(s)
        opening,closing, swaps = 0, 0, 0
        l = 0
        r = n - 1
        for i in range(n):
            if s[i] == '[':
                opening += 1
            else:
                closing += 1
            if closing > opening and l < r:
                s[l], s[r] = s[r], s[l]
                swaps += 1
                r -= 1
                l += 1
                closing -= 1
                opening += 1
        return swaps