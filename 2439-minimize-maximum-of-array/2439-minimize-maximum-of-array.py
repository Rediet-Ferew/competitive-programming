class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = 0
        result = 0
        for i, num in enumerate(nums, start = 1):
            total += num
            result = max(ceil(total/i), result)
        return result