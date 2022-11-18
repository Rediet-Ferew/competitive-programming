class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        bit = 0
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                if bit == 1:
                    return False
                bit += 1
                if i >= 2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
        return True