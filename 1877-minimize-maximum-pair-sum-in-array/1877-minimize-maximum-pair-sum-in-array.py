class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        
        
        """
        nums = sorted(nums)
        max_sum = 0
        for i in range(0, len(nums)//2):
            max_sum = max(max_sum, (nums[i] + nums[-1]))
            nums.pop()
        
        return max_sum