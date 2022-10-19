class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]
        right = [1] * (n + 1)
        result = []
        prod = 1
        for i in range(n):
            prod *= nums[i]
            left.append(prod)
        prod2 = 1
        for j in range(n - 1, -1, -1):
            prod2 *= nums[j]
            right[j] = prod2
        for k in range(n):
            mul = left[k] * right[k + 1]
            result.append(mul)
        return result
        
            