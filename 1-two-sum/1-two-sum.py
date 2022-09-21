class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        
        # for i in range(len(nums)):
        #     end = len(nums) - 1
        #     while i < end:
        #         indices[nums[i] + nums[end]] = (i, end)
        #         end -= 1
        # # print(indices)
        # for key, value in indices.items():
        #     if key == target:
        #         return (indices[key])
                
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    indices.append(i)
                    indices.append(j)
                    break
        return indices