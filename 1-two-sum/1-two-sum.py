class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force approach
        # indices = []
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             indices.append(i)
        #             indices.append(j)
        #             break
        # return indices
        prefix = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prefix:
                return [prefix[diff], i]
            prefix[num] = i
        return
       
                
        