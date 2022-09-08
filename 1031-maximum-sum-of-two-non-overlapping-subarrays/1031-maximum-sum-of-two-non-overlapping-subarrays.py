class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefixSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        # print(prefixSum)
        def findSum(prefix, firstlength, secondlength):
            max1 = 0
            max2 = 0
            for i in range(len(prefix) - firstlength - secondlength):
                firstSum = prefix[i + firstlength] - prefix[i]
                secondSum = prefix[i + firstlength + secondlength] - prefix[i + firstlength]
                max1 = max(max1, firstSum)
                max2 = max(max2, max1 + secondSum)
            return max2
        maxSum1 = findSum(prefixSum, firstLen, secondLen)
        maxSum2 = findSum(prefixSum, secondLen, firstLen)
        # print(maxSum1)
        # print(maxSum2)
        return max(maxSum1, maxSum2)