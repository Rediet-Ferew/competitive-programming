class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        final = [0] * n
        l = 0
        r = n - 1
        for i in range(len(nums)):
            if nums[i] < pivot:
                final[l] = nums[i]
                l += 1
            if nums[n - i - 1] > pivot:
                final[r] = nums[n - i - 1]
                r -= 1
        while l <= r:
            final[l] = pivot
            l += 1
        return final
        