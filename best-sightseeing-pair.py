class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp = [0] * n
        dp[1] = values[0] + values[1] - 1
        ans = dp[1]

        for i in range(2, n):
            dp[i] = max(dp[i-1]-values[i-1]+values[i]-1,values[i-1]+values[i]-1)
            ans = max(dp[i], ans)
        
        return ans