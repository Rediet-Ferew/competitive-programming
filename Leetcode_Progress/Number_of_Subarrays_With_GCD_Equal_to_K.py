class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def check(a, b):
            if b == 0:
                return a
            else:
                return check(b, a % b)
        cnt = 0
      
        for i in range(len(nums)):
            
            hcf = nums[i]
            
            for j in range(i , len(nums)):
                hcf = check(hcf, nums[j])
                
                if hcf == k:
                    cnt += 1
        return cnt
        
