class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def dp(nums):
            memo = [0] * (len(nums))
            memo[0] = nums[0]
            memo[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])
            return max(memo[-2], memo[-1])
        

        if n <= 2:
            m = max(nums)
            return max(m, 0)
        return max(dp(nums[1:]), dp(nums[:-1]))