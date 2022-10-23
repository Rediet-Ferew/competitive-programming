class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefixSum = [0]
        suffixSum = [0] * (len(nums) + 1)
        result = []
        n = len(nums)
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            prefixSum.append(pre)
        suff = 0
        for j in range(len(nums) - 1, -1, -1):
            suff += nums[j]
            suffixSum[j] = suff
        for idx, num in enumerate(nums):
            left = (num * idx) - prefixSum[idx]
            right = suffixSum[idx + 1] - (num * (n - idx - 1)) 
            result.append(left + right)
        return result