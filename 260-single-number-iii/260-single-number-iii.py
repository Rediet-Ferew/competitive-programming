class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        once = []
        count = Counter(nums)
        for num in nums:
            if count[num] == 1:
                once.append(num)
        return once