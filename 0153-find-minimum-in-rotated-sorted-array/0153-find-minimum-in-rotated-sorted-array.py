class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_val = float('inf')
        while l <= r:
            m=(l+r)//2
            if nums[l] <= nums[m]:
                min_val = min(min_val, nums[l])
                l = m + 1
            else:
                min_val = min(min_val, nums[m])
                r = m - 1
        return min_val