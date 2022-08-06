class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        products = []
        prod1 = 1
        prod2 = 1
        for i in range(len(nums)):
            prod1 = math.prod(nums[: i])
            prod2 = math.prod(nums[i + 1:])
            
            products.append(prod1 * prod2)
        return products