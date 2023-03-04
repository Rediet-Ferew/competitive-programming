class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def find_sum(nums, divisor):
            total = 0
            for num in nums:
                total += math.ceil((num) / divisor)
            return total
        
        left = 1
        right = max(nums)
        min_divisor = -1
        while left <= right:
            mid = (left + right) // 2
            
            avrg = find_sum(nums, mid)
            
            if avrg <= threshold:
                
                min_divisor = mid
                right = mid - 1
                
            elif avrg > float(threshold):
                left = mid + 1
            
        
        
        return (min_divisor)