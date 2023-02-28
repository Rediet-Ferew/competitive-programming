class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        left = 0
        right = k
        total = sum(nums[left:right])
        avrg = total/k
        max_avrg = max(avrg, float('-inf'))
        while right < n:
            total -= nums[left]
            total += nums[right]
            curr_avrg = total/k
            max_avrg = max(max_avrg, curr_avrg)
            left += 1
            right += 1
        return max_avrg