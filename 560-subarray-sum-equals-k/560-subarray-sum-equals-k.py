class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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