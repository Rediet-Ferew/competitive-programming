class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            
            if mid > 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            elif mid < n - 1 and nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                return mid
        
        