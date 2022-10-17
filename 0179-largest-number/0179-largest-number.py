class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        # temp = nums[0]
        # for ch in nums[1: ]:
        #     cmp1 = temp + ch
        #     cmp2 = ch + temp
        #     if cmp1 > cmp2:
        #         temp = cmp1
        #     else:
        #         temp = cmp2
        # return temp
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key = cmp_to_key(compare))
        largest = int("".join(nums))
        return str(largest)