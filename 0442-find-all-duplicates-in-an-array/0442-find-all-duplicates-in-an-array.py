class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        start = 0
        ans = set()
        while start < len(nums):
            idx = nums[start] - 1
            if idx == start:
                start += 1
                continue
            if nums[idx] == nums[start]:
                ans.add(nums[idx])
                start += 1
            else:
                nums[start], nums[idx] = nums[idx], nums[start]
        return ans