class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        [1,2,5,2,3]
        b = 1
        t = 2
        [1,2,2,3,5]
        1, 
        """
        output = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if num == target:
                output.append(i)
        return output