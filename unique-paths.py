class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}
        def isInBound(r, c):
            return r >= 0 and r < m and c >= 0 and c < n
        # @cache
        # def dp(r, c):
        #     if r == m - 1 and c == n - 1:
        #         return 1
        #     ways = 0
            
        #     if isInBound(r + 1, c):
        #         ways += dp(r + 1, c) 
            
        #     if isInBound(r, c + 1):
        #         ways += dp(r, c + 1)
        #     return ways
            
        # return dp(0, 0)
        dp = []
        for i in range(m):
            temp = [0] * n
            dp.append(temp)
        dp[0][0] = 1
        for r in range(m):
            for c in range(n):
                #find the top and left
                #top
                if isInBound(r - 1, c):
                    dp[r][c] += dp[r - 1][c]
                if isInBound(r, c - 1):
                    dp[r][c] += dp[r][c - 1]
        return dp[m - 1][n - 1]