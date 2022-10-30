class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        k = 0
        temp = 1
        while k < 2:
            if nums[k] < 0: 
                temp *= (-1 * nums[k])
                k += 1
            else:
                k += 1
                continue
        if temp > 1:
            temp *= nums[-1]
        else:
            temp = 0
      
        prod = 1
        for i in range(n - 1, n - 4, -1):
            prod *= nums[i]
        
        return temp if temp > prod else prod
        