class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #Brute-Force
        # if len(nums) == 1:
        #     return False
        # total = nums[0]
        # for right in range(1, len(nums)):
        #     total += nums[right]
        #     if total % k == 0:
        #         return True
        #     else:
        #         left = 0
        #         num = total
        #         while right - left > 1:
        #             num -=  nums[left]
        #             if num % k == 0:
        #                 return True
        #             left += 1
        # return False
        prefix = {0 : -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            mod = total % k
            if mod in prefix and (i - prefix[mod]) > 1:
                return True
            elif mod not in prefix:
                prefix[mod] = i
        return False