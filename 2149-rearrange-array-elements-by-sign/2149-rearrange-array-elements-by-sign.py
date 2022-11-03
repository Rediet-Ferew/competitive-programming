class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        final = [0] * len(nums)
        even = 0
        odd = 1
        for num in nums:
            if num > 0:
                final[even] = num
                even += 2
            else:
                final[odd] = num
                odd += 2
        return final