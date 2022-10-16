class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        # right = 1
        for right in range(1, len(nums)):
            if nums[right - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
        return left
        # while left < right and right < len(nums):
        #     while nums[left] == nums[right]:
        #         del nums[right]
        #     right += 1
        #     left += 1
        # print(nums)
        
        