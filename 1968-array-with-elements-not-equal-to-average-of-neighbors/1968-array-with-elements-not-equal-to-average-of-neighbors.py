class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        mid = n // 2
        median = 0.0
        if n % 2 == 0:
            median =(nums[mid] + nums[mid - 1]) / 2
        else:
            median = float(nums[mid])
        even = 0
        odd = 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            if float(nums[i]) < median:
                res[odd] = nums[i]
                odd += 2
            else:
                res[even] = nums[i]
                even += 2
        return res