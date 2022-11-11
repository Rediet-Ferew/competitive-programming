class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        2, 3, 4, 4, 5,6 
        """
        nums.sort()
        l = 0
        r = len(nums) - 1
        max_sum = 0
        while l < r:
            max_sum = max(max_sum, nums[l] + nums[r])
            l += 1
            r -= 1
        return max_sum
        