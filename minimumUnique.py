class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        setted = set(nums)
        nums = sorted(nums)
        counter = 0
        while len(nums) != len(setted):
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    nums[i + 1] += 1
                    counter += 1
                nums = sorted(nums)
                setted = set(nums)
        return counter