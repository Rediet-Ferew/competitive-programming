class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix = sum(nums)
        pre = 0
        result = []
        for idx, num in enumerate(nums):
            suffix -= num
            left = (num * idx) - pre
            right = suffix - (num * (n - idx - 1))
            result.append(left + right)
            pre += num
        return result
        