class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        r = 0
        prod = 1
        result = 0
        while r < len(nums):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod = prod // nums[l]
                l += 1
            result += (r - l + 1)
            r += 1
        return result