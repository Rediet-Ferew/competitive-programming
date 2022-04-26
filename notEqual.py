class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 3 and len(nums) <= 100000:
            for i in range(1, len(nums) - 1):
                if nums[i] >= 0 and nums[i] <= 100000:
                    if (nums[0] >= 0 and nums[0] <= 100000) and nums[len(nums) - 1] >= 0 and nums[len(nums) - 1] <= 100000:
                        if (nums [i - 1] + nums [i + 1]) / 2 == nums[i]:
                                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                for j in range(len(nums) - 1, 0):
                    if nums[j] >= 0 and nums[j] <= 100000:
                        if (nums[0] >= 0 and nums[0] <= 100000) and nums[len(nums) - 1] >= 0 and nums[len(nums) - 1] <= 100000:
                            if (nums [j - 1] + nums [j + 1]) / 2 == nums[j]:
                                nums[j], nums[j - 1] = nums[j - 1], nums[j]
        elif len(nums) == 3:
            if nums[1] == (nums[0] + nums[2])/2:
                nums[0], nums[1] = nums[1], nums[0]
        return nums
            