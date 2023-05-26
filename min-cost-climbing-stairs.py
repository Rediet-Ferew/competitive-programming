class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dp(i):
            if i >= n:
                return 0
            if i not in memo:
                memo[i] = min(cost[i] + dp(i + 1), cost[i]+ dp(i + 2))
            return memo[i]

        return min(dp(0), dp(1))