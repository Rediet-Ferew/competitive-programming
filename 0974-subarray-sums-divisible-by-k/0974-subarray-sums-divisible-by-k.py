class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        prefix = {0:1, 4:3,2:1}
        [4,5,0,-2,-3,1]
        
        sum = 5
        count = 7
        k = 5
        if we get the same remainder then th
        """
        n = len(nums)
        mods = {0:1}
        total = 0
        subarrays = 0
        
        for i in range(n):
            total += nums[i]
            mod = total % k
            
            if mod in mods:
                
                subarrays += mods[mod]
                mods[mod] += 1
                
            else:
                
                mods[mod] = 1
                
        return subarrays