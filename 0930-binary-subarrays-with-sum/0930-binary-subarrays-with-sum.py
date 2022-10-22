class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {0: 1}
        result = 0
        total = 0
        for binary in nums:
            total += binary
            target = total - goal
            if target in prefix:
                result += prefix[target]
                
            prefix[total] = prefix.get(total, 0) + 1
        return result
             