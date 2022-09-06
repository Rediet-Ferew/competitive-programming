class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        sum_array = []
        for i in range(0, len(nums)//2):
            sum_array.append(nums[i] + nums[-1])
            nums.pop()
        
        return max(sum_array)