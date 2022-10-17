class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        nums.sort()
        for i, num in enumerate(nums):
            if num == target:
                output.append(i)
        return output