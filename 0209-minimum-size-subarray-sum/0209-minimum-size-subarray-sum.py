class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        minimal = float("inf")
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                minimal = min((right - left + 1), minimal)
                total -= nums[left]
                left += 1
        return 0 if minimal == float("inf") else minimal
            
#         prefix = []
#         summation = 0
#         minimal = 0
#         for num in nums:
#             summation += num
#             prefix.append(summation)
#         for i in range(len(prefix)):
#             if prefix[i] >= target:
#                 minimal = (len(nums) - 1) - i
#                 break
#         print(minimal)
        