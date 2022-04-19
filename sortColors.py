class Solution:
    def sortColors(self, nums: List[int]) -> None:
       
        n = len(nums)
        if n >= 1 and n <= 300:
            for j in range(0, n):
                if nums[j] == 0 or nums[j] == 1 or nums[j] == 2:
                    minIndex = j 
                    for i in range(j, n):
                        if nums[i] < nums[minIndex]:
                            minIndex = i
                    nums[j], nums[minIndex] = nums[minIndex], nums[j]
            print(nums)

            
 
        
        