class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         n = len(nums)
#         for i in range(n):
#             if nums[i] == 0:
#                 del nums[i]
#                 nums.insert(0, 0)
#             elif nums[i] == 2:
#                 del nums[i]
#                 nums.insert(n - 1, 2)
                
#         print(nums)
        n = len(nums)
        if n >= 1 and n <= 300:
            for j in range(0, n):
                minIndex = j 
                for i in range(j, n):
                    if nums[i] < nums[minIndex]:
                        minIndex = i
                nums[j], nums[minIndex] = nums[minIndex], nums[j]
            