class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        min_sum = float("inf")
        @cache
        def recursion(i, sum_):
            nonlocal min_sum
            if i == n:
                if sum_ >= 0:
                    min_sum = min(min_sum, sum_)
                return sum_
            min_val = float("inf")
            min_val = min(recursion(i + 1, sum_ + stones[i]),
            recursion(i + 1, sum_ - stones[i]))
            return min_val
        recursion(0, 0)
        return min_sum