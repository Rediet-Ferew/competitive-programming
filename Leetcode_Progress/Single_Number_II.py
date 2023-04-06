class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_mask = 1
        res = 0
        # cnt = 0
        
        for i in range(32):
            cnt = 0
            
            for j in range(len(nums)):
                if (nums[j] & bit_mask) != 0:
                    cnt += 1
            if (cnt % 3 != 0):
                res |= bit_mask
            bit_mask *= 2
        return res if res < (1 << 31) else res - (1 << 32)
