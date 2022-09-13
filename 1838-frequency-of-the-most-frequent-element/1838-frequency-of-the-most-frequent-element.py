class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = 0
        total = 0
        result = 0
        
        while right < n:
            total += nums[right]
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result