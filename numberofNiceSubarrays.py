class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range (len(nums)):
            if nums[i]%2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        counter = 0
        summation = 0
        prefixSum = {0 : 1}
        for n in nums:
            summation += n
            case = summation - k
            if prefixSum.get(case):
                counter += prefixSum.get(case)
            prefixSum[summation] = prefixSum.get(summation, 0) + 1
        return counter