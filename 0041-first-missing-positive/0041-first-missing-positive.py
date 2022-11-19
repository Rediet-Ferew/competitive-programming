class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:                
        nums.sort()
        pos = 1
        
        for n in nums:
            if n == pos:
                pos+=1
        return pos
                