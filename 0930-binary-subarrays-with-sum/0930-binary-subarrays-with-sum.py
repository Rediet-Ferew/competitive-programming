class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix = {0 : 1}
        total = 0
        subarrays = 0
        for right in range(n):
            
            total += nums[right]
            diff = total - goal
            
            if diff in prefix:
                subarrays += prefix[diff]
                
            if total in prefix:
                
                prefix[total] += 1
                
            else:
                prefix[total] = 1
        return subarrays