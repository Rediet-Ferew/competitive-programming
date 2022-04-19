class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        countList = []
        if len(nums) > 2 and len(nums) <= 500:
            for i in range(0, len(nums)):
                counter = 0
                if nums[i] >=0 and nums[i] <= 100:
                    for j in range(0, len(nums)):
                        if nums[j] < nums[i]:
                            counter += 1
                countList.append(counter)
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                countList.append(1)
                countList.append(0)
            else:
                countList.append(0)
                countList.append(1)
                    
        return countList