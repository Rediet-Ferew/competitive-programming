class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atmost(nums, k):
            left = 0
            right = 0
            odd_count = 0
            subarrays = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    odd_count += 1
                while odd_count > k:
                    if nums[left] % 2 != 0:
                        odd_count -= 1
                    left += 1
                subarrays += (right - left + 1)
                
            return subarrays
        
        ans = atmost(nums, k) - atmost(nums, k - 1)
        return ans
