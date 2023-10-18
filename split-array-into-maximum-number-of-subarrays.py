class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        b = (2 ** 32) - 1
        n = len(nums)
        all_and = b
        for num in nums:
            all_and &= num
        
        if all_and > 0:
            return 1
        # curr_and = nums[0]
        i = 0
        cnt = 0
        while i < n:
            curr_and = b
            # print(curr_and)
            
            j = i
            while j < n:
                curr_and &= nums[j]
                if curr_and != 0:
                    j += 1
                else:
                    cnt += 1
                    break
            
            # cnt += 1
            i = j + 1
        # print(cnt)
        return cnt