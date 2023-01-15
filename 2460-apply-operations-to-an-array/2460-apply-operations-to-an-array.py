class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = 2*nums[i]
                nums[i+1] = 0
            else:
                continue
        r = 0
        s = 0
        while r < len(nums):
            if nums[r] != 0 and nums[s] != 0:
                s += 1
                r += 1
            elif nums[r] != 0 and nums[s] == 0:
                nums[r], nums[s] = nums[s], nums[r]
                s += 1 
                r += 1
            elif nums[r] == 0 and nums[s] == 0:
                r += 1
        return nums