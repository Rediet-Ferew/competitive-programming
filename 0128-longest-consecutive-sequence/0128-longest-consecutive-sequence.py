class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        n = len(nums)
        max_con = 0
        curr_longest = 1
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                curr_longest += 1
            else:
                max_con = max(curr_longest, max_con)
                curr_longest = 1
        return max(max_con,curr_longest)