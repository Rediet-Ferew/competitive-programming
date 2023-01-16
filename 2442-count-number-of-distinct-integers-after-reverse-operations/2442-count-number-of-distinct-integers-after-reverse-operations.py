class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        
        for idx in range(n):
            
            num = nums[idx]
            rev_digit = 0
            
            while num > 0:
                mod = num % 10
                rev_digit = 10 * rev_digit + mod
                num = num // 10
                
            nums.append(rev_digit)
        
        ans = len(set(nums))
        
        return ans
        