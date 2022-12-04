class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        l = len(nums)
        prefix = 0
        suffix = sum(nums)
        min_diff = [float('inf'), 0]
        for i, n in enumerate(nums[:-1]):
            prefix += n
            suffix -= n
            diff = abs(int(suffix/(l-i-1)) - int(prefix/(i+1)))
            if diff < min_diff[0]:
                min_diff[0] = diff
                min_diff[1] = i
        prefix += nums[-1]
        diff = abs(0 - int(prefix/l))
        if diff < min_diff[0]:
                min_diff[0] = diff
                min_diff[1] = l-1
        return min_diff[1]