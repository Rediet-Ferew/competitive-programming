class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        idx = 0
        l = 0
        r = n - 1
        if target not in nums:
            nums.append(target)
            nums.sort()
            # return (nums.index(target))
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        idx = max(l, r)
        return idx
        
                
        #     if nums[n // 2] == target:
        #         idx += (n//2 - 1)
        #     elif nums[n // 2] < target:
        #         idx += (n//2 )
        #         nums = nums[(n // 2) + 1:]
        #     elif nums[n // 2] > target:
        #         idx += (n// 2 - 1)
        #         nums = nums[: (n // 2) + 1]
        #     n = n // 2
        # print(nums)
        # print(idx)