class Solution:
    def numberOfWays(self, s: str) -> int:
        c0 = 0
        c1 = 0
        for ch in s:
            if ch == "0":
                c0 += 1
            else:
                c1 += 1
        value = 0
        count_zero = 0
        count_one = 0
        for i in range(len(s)):
            if s[i] == "0":
                value += count_one * (c1 - count_one)
                count_zero += 1
            else:
                value += count_zero * (c0 - count_zero)
                count_one += 1
        return value