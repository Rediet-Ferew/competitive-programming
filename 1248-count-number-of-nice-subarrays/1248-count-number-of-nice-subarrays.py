class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        for i in range(n):
            if nums[i] % 2 != 0:
                nums[i] = 1
            else:
                nums[i] = 0
#         odd_count = 0
#         left = 0
#         right = 0
#         subarrays = 0
#         for right in range(n):
#             if nums[right] == 1:
#                 odd_count += 1
#             while odd_count == k:
#                 subarrays += 1
#                 if nums[left] == 1:
#                     odd_count -= 1
#                 left += 1
        
#         return subarrays
                
        counter = 0
        summation = 0
        prefixSum = {0 : 1}
        for i in nums:
            summation += i
            case = summation - k
            if prefixSum.get(case):
                counter += prefixSum.get(case)
            prefixSum[summation] = prefixSum.get(summation, 0) + 1
        return counter