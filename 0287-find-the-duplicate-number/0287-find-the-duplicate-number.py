class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 0
        while start < len(nums):
            idx = nums[start] - 1
            if idx == start:
                start += 1
                continue
            if nums[idx] == nums[start]:
                return nums[idx]
            else:
                nums[start], nums[idx] = nums[idx], nums[start]