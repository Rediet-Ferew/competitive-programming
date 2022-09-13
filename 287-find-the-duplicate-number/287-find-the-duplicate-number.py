class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        print(count)
        for key, val in count.items():
            if count[key] > 1:
                return key