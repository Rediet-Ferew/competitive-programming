class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                output.append(i)
        return output