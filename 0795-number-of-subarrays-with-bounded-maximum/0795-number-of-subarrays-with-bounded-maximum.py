class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        l = -1
        r = -1
        n = len(nums)
        counter = 0
        for i in range(n):
            if nums[i] >= left:
                l = i
            if nums[i] > right:
                r = i
            counter += (l - r)
        return counter