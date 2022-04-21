class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indexList = []
        for j in range(0,len(nums)): 
            minIndex = j 
            for i in range(j, len(nums)):
                if nums[i] < nums[minIndex]:
                    minIndex = i
            nums[j], nums[minIndex] = nums[minIndex], nums[j]
        for k in range(0, len(nums)):
            if (nums[k] >=1 and nums[k] <= 100) and nums[k] == target:
                indexList.append(k)
        return indexList
        