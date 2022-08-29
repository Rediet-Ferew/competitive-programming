class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        length = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                subArray = nums[i : j]
                if max(subArray) - min(subArray) <= limit:
                    length = max(length, len(subArray))
        return length