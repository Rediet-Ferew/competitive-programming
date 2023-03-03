class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect_left(nums, target)
        end = bisect_right(nums, target)
        
        if not nums:
            return [-1, -1]
        elif start > len(nums) - 1 or nums[start] != target:
            return [-1, -1]
        
        return [start, end - 1]
        # def binary_search(nums):
        #     l = 0
        #     r = len(nums) - 1 
        #     while l <= r:
        #         m = (l+r)//2
        #         if nums[m] == target:
        #             return m
        #         elif nums[m] < target:
        #             l = m + 1
        #         else:
        #             r = m - 1
        #     return -1
        # t_idx = binary_search(nums)
        # if t_idx == -1 or len(nums) == 0:
        #     return [-1, -1]
        # left = t_idx
        # right = t_idx
        # while left > 0 and nums[left - 1] == target:
        #     left -= 1
        # while right < len(nums) - 1 and nums[right + 1] == target:
        #     right += 1
        # return [left, right]