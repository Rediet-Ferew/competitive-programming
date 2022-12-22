class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        num = 0
        for i in range(n):
            if nums[i] != num:
                return num
            num += 1
        return num