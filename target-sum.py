class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        ans = 0
        n = len(nums)
        def dp(idx, sum_):
            
            if idx == len(nums):
                if sum_ == target:
                    return 1
                else:
                    return 0
            if (idx, sum_) in memo:
                return memo[(idx, sum_)]
            if (idx, sum_) not in memo:
                memo[(idx, sum_)] = (dp(idx + 1, sum_ + (nums[idx])) + dp(idx + 1, sum_ - (nums[idx])))
                

            return memo[(idx, sum_)]

        return dp(0, 0)