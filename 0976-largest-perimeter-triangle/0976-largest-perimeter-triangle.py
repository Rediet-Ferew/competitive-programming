class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        l = 0
        r = 1
        last = 2
        p = 0
        while last < n:
            if (nums[l] + nums[r]) > nums[last]:
                perimeter = nums[l] + nums[r] + nums[last]
                p = max(p, perimeter)
            l += 1
            r += 1
            last += 1
        return p
            