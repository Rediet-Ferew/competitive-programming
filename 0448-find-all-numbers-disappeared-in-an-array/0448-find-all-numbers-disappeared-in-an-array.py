class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        start = 0
        # ans = set()
        while start < len(nums):
            idx = nums[start] - 1
            if idx == start:
                start += 1
                continue
            if nums[idx] == nums[start]:
                
                start += 1
            else:
                nums[start], nums[idx] = nums[idx], nums[start]
        ans = []
        for i in range(len(nums)):
            if i != nums[i] - 1:
                ans.append(i + 1)
        return ans