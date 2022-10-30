class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(1, len(nums) - 1):
            temp = nums[i] - diff
            temp2 = diff + nums[i]
            if temp in nums[:i] and temp2 in nums[i + 1:]:
                count += 1
        return count