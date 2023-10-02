class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        max_sum = float("-inf")
        memo = {}
        def dp(i, time):
            nonlocal max_sum
            
            if i == n - 1:
                return ((time + 1) * satisfaction[i])
            if i >= n:
                
                return float("-inf")
            if (i, time) in memo:
                return memo[(i, time)]
            max_val = float("-inf")

            val_1 = dp(i + 1, time + 1) + (satisfaction[i] * (time + 1))
            val_2 = dp(i + 1, time)
            memo[(i, time)] = max(val_1, val_2)

            return memo[(i, time)]
        ans = dp(0, 0)
        if ans <= 0:
            return 0
        return ans
        # return max_sum