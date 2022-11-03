class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lcount = 0
        gcount = 0
        final = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > pivot:
                gcount += 1
            elif nums[i] < pivot:
                lcount += 1
        
        l = 0
        g = len(nums) - gcount
        m = lcount
        for j in range(len(nums)):
            if nums[j] < pivot:
                final[l] = nums[j]
                l += 1
            elif nums[j] > pivot:
                final[g] = nums[j]
                g += 1
            else:
                final[m] = nums[j]
                m += 1
        return final