class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0
        left, right = 0, 0
        counter = 0
        while right < n:
            if nums[right] == 0:
                counter += 1
            while counter > 1 and left < n:
                if nums[left] == 0:
                    counter -= 1
                left += 1
            right += 1
            longest = max(longest, right - left - 1)
        return longest
                