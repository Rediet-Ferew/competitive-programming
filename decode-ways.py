class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dp(i):
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]
            if s[i] == "0":
                return 0
            ways = dp(i + 1)
            if (i + 1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                ways += dp(i + 2)
            memo[i] = ways
            return ways
        return dp(0)