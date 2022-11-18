class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = float('inf')
        if n == 1 or k == 1:
            return 0
        for i in range(n-k+1):
            diff = nums[i+(k-1)] - nums[i]
            min_diff = min(diff, min_diff)
        return min_diff