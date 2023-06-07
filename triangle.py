class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        dp = [0] * (n+1)
        triangle.reverse()
        for t in triangle:
            for i,n in enumerate(t):
                dp[i] = n + min(dp[i], dp[i+1])
        return dp[0]