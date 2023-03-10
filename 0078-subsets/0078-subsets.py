class Solution:
    def backtrack(self, start, arr, res, nums):
        if start >= len(nums):
            return 
        
        for i in range(start, len(nums)):
            arr.append(nums[i])
            # print(arr)
            res.append(arr.copy())
            self.backtrack(i + 1, arr, res, nums)
            arr.pop()
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        bucket = []
        result = [[]]
        self.backtrack(0, bucket, result, nums)
        return result