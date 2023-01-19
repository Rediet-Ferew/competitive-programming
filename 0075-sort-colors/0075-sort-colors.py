class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        zero = 0
        end = len(nums) - 1
        
        while l <= end:
            if nums[l] == 0:
                nums[l], nums[zero] = nums[zero], nums[l]
                l += 1
                zero += 1
            elif nums[l] == 1:
                l += 1
            else:
                nums[l], nums[end] = nums[end], nums[l]
                end -= 1
        
