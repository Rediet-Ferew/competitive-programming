class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        for num in range(0, max(nums) + 2):
            if num not in nums:
                return num
        