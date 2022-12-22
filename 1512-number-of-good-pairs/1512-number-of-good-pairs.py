class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        pairs = 0
        for k, v in count.items():
            pair = (v*(v-1))//2
            pairs += pair
        return pairs