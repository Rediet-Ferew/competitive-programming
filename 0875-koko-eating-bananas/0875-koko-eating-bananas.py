class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(num, arr):
            total_hr = 0
            for pile in arr:
                if pile <= num:
                    total_hr += 1
                else:
                    total_hr += (math.ceil(pile/num))
            return total_hr 
                    
        low = 1
        high = max(piles)
        min_banana = high
        
        while low <= high:
            
            mid = (low + high) // 2
            
            curr_hr = check(mid, piles)
            
            if curr_hr <= h:
                min_banana = min(min_banana, mid)
                high = mid - 1
            else:
                low = mid + 1
                
        return min_banana
            