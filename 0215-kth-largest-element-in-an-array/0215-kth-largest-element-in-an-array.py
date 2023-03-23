class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums)- k
        def quickSort(start, end):
            if start == end:
                return nums[start]
            pivot = nums[start]
            l = start + 1
            r = start + 1
            while  r <= end:
                if nums[r] < pivot:
                    nums[r],nums[l] = nums[l], nums[r]
                    l += 1
                r += 1
            nums[start],nums[l-1] = nums[l-1], nums[start]
            if l - 1 == target:
                return nums[l-1]
            elif target > l -1:
                return quickSort(l,end)
            else:
                return quickSort(start,l-2)

        return quickSort(0,len(nums)-1)