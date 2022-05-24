class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        counter = 0
        newList = []
        
        nums = nums[(counter):]
        for j in range(len(nums) - 1):
            for i in range(j + 1, len(nums)):
                if nums[j] == nums[i]:
                    counter += 1
                else:
                    break
            newList.append(nums[j])
            
            
            
        
        return list(set(newList))