class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for key, val in count.items():
            if count[key] == 1:
                return key