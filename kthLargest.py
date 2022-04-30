class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = len(nums)
        for j in range(0, n): 
            minIndex = j 
            for i in range(j, n):
                if nums[i] < nums[minIndex]:
                    minIndex = i
            nums[i], nums[minIndex] = nums[minIndex],nums[i]
        return str(nums[-k])