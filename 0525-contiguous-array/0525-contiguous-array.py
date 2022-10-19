class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {}
        summation = 0
        max_len = 0
        for i, num in enumerate(nums):
            if num == 0:
                summation -= 1
            elif num == 1:
                summation += 1
            if summation == 0:
                max_len = i + 1
            elif summation not in prefix:
                prefix[summation] = i
            elif summation in prefix:
                length = i - prefix[summation]
                max_len = max(max_len, length) 
        return max_len
                
                