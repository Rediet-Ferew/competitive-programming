class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        counter = 0
        for i in range(len(nums) - 1):
            for j in range(i+1 , len(nums)):
                if nums[i] == nums [j] and i < j:
                    counter += 1
                    continue
                    
        return counter
                    
                