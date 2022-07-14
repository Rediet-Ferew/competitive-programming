class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        
        for i in range(0, k):
            for j in range(len(nums) - 1):
                for p in range(j + 1, len(nums)):
                    if nums[j] == nums[p]:
                        continue
                    else:
                        nums[j] += 1
                 
            from itertools import groupby
            count = [len(list(group)) for key, group in groupby(sorted(nums))]
        print(count)
        return max(count)
       
            