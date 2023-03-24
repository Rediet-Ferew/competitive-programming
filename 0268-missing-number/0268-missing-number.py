class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        ans = set()
        while start < len(nums):
            idx = nums[start]
            if idx == start:
                start += 1
                continue
            if idx == n:
                start += 1
                continue
            
            else:
                nums[start], nums[idx] = nums[idx], nums[start]
        for i in range(n):
            if i != nums[i]:
                return i
        return n
        