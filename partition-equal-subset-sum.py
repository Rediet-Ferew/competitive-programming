class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums) // 2
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False
        @cache
        def dp(i, target):
            if target == 0:
                return True
            
            if target < 0 or i == n:
                return False
            # if (i, target) in memo:
            #     return memo[(i, target)] 
            
            if dp(i + 1, target) or dp(i + 1, target - nums[i]):
                # memo[(i, target)] = True
                return True
            
            # memo[(i, target)] = False
            return False

        return dp(0, sum_)