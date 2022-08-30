class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1
            if k < 0:
                k += (1 - nums[start])
                start += 1
            max_length = max(max_length, i - start + 1)
        return max_length