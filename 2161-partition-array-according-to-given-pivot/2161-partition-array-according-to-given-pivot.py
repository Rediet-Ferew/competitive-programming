class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        middle = []
        greater = []
        final = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] > pivot:
                greater.append(nums[i])
            else:
                middle.append(nums[i])
        for n in less:
            final.append(n)
        for n in middle:
            final.append(n)
        for n in greater:
            final.append(n)
        return final