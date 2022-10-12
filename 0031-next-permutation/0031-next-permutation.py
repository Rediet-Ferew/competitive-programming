class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 2:
            nums.reverse()
            return
        pivot = n - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
        if pivot == -1:
            nums.reverse()
            return
        
        for i in range(n - 1, pivot, -1):
            if nums[pivot] < nums[i]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
            