class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        if len(stones) == 1:
            return stones[0]
        while len(stones) > 1:
            first = stones.pop()
            second = stones.pop()
            stones.append(first - second)
            stones = sorted(stones)
        return stones[0]