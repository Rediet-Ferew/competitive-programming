class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        left = 0
        right = k 
        total = sum(nums[:k])
        curr_avr = total / k
        max_avr = curr_avr
        while right < n:
            total -= nums[left]
            total += nums[right]
            # print(total)
            curr_avr = total / k
            # print(curr_avr)
            max_avr = max(max_avr, curr_avr)
            left += 1
            right += 1
        return max_avr
        # return 0
            