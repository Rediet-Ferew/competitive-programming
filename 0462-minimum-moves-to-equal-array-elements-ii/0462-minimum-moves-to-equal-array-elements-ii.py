class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) 
        if len(set(nums)) == 1:
            return 0
        prefix = 0
        suffix = sum(nums)
        min_moves = float("inf")
        for i in range(n):
            suffix -= nums[i]
            moves_before = abs(prefix - (nums[i]*i))
            moves_after = suffix - ((n-i-1)*nums[i])
            min_moves = min(min_moves, (moves_before+moves_after))
            prefix += nums[i]
        return min_moves
        