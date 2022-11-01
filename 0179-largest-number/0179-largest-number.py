class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        nums = sorted(nums, key = cmp_to_key(compare))
        res = int("".join(nums))
        return str(res)