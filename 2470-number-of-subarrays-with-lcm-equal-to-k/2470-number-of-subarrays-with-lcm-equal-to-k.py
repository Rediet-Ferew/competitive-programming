class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        counter = 0
        for i in range(len(nums)):
            temp_lcm = nums[i]
            for j in range(i, len(nums)):
                temp_lcm = lcm(temp_lcm, nums[j])
                if temp_lcm == k:
                    counter += 1
                elif temp_lcm > k:
                    break
        return counter
        