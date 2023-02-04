class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_min  = 0
        for idx in range(len(nums)):
            if idx % 2 == 0:
                max_min += nums[idx]
                
        return max_min