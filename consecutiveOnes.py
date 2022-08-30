class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        start = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_length = (i - start)
                start = i + 1
        max_length = max(max_length, (len(nums) - 1) - start + 1)
            
        return max_length