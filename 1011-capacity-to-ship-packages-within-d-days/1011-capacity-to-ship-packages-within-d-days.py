class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        n = len(weights)
        def check(num, arr):
            
            total_hr = 1
            curr_sum = 0
            for i in range(n):
                curr_sum += weights[i]
                if curr_sum > num: 
                    total_hr += 1
                    curr_sum = arr[i]
                
            return total_hr
    
                    
        low = max(weights)
        high = sum(weights)
        min_weight = 0
        
        while low <= high:
            
            mid = (low + high) // 2
            
            curr_hr = check(mid, weights)
            
            if curr_hr <= days:
                
                min_weight = mid
                high = mid - 1
                
            else:
                
                low = mid + 1
                
        
        return min_weight