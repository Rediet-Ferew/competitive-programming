class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums.sort()
        numset = list(set(nums))
        numset.sort()
        if len(numset) <= 2:
            return max(numset)
        else:
            numset.pop()
            numset.pop()
            return numset[-1]
            