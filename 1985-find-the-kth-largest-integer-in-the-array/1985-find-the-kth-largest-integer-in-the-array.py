class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(num) for num in nums]
        n = len(nums)
        nums = sorted(nums)[::-1]
        print(nums)
        return str(nums[k - 1])