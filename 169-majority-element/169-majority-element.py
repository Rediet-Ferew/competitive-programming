class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        print(freq)
        n = len(nums) // 2
        for k, v in freq.items():
            if v > n:
                return k
        