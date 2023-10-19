class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        #decrease the maximum
        #increase the minimum
        if len(nums) == 1:
            return 0
        decreased_max = max(nums) - k
        increased_min = min(nums) + k
        diff = decreased_max - increased_min
        if diff <= 0:
            return 0
        return diff