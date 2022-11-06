class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                diff = nums[i-1] + 1 - nums[i]
                moves += diff
                nums[i] = nums[i-1] + 1
        return moves
        #TLE
        # checker = {}
        # moves = 0
        # for i, num in enumerate(nums):
        #     if num not in checker:
        #         checker[num] = i
        #     else:
        #         while num in checker:
        #             num += 1
        #             moves += 1
        #         checker[num] = i
        # return moves