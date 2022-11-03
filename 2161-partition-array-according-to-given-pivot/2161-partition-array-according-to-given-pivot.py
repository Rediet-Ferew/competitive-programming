class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        count = {
            -1 : 0,
            1 : 0,
            0 : 0
        }
        
        less = []
        middle = []
        greater = []
        final = [0] * len(nums)
        
        for i in range(len(nums)):
            if nums[i] > pivot:
                count[1] += 1
            elif nums[i] < pivot:
                count[-1] += 1
            else:
                count[0] += 1
        
        l = 0
        g = len(nums) - count[1]
        m = count[-1]
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
        # for n in less:
        #     final.append(n)
        # for n in middle:
        #     final.append(n)
        # for n in greater:
        #     final.append(n)
        return final