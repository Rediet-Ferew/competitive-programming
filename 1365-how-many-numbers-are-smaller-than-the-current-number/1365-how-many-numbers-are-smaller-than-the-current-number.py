class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        indices = {}
        sorted_nums = sorted(nums)
        
        for idx, num in enumerate(sorted_nums):
            
            if num in indices:
                continue
            else:
                indices[num] = idx
        
        
        for i, m in enumerate(nums):
            
            ans[i] = indices[m]
        
        return ans