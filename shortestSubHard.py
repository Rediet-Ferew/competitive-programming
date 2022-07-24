class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        counter = 0
        summation = 0
        for i in range(len(nums)):
            summation += nums[i]
            if k in nums:
                counter = 1
            elif summation == k:
                counter = i + 1
                break
            else:
                counter = -1
        return counter
            