class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        
        for num in nums:
            if num != max_num and max_num < (2*num):
                return -1
            
        return nums.index(max_num)