class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        preSum = {0:1}
        result = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            mod = total % k
            if mod in preSum:
                result += preSum[mod]
                preSum[mod] += 1
            else:
                preSum[mod] = 1
        return result