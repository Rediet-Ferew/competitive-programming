class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {0: 1}
        for num in range(1, target + 1):
            memo[num] = 0
            for n in nums:
                if num - n not in memo:
                    memo[num - n] = 0
                memo[num] += memo[num - n]
        return memo[target]