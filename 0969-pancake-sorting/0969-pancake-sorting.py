class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        def flip(left, right, nums):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
                
        n = len(arr)  
        pancake_flips = [] 
        arr_sorted = sorted(arr)
        
        max_idx = n - 1
        end = n - 1
        
        while end >= 0 and max_idx >= 0:
            
            num = arr_sorted[max_idx]
            max_num = arr.index(num)
            
            if max_num != max_idx:
                
                pancake_flips.append(max_num + 1)
                flip(0, max_num, arr)
                
                pancake_flips.append(end + 1)
                flip(0, end, arr)
                
            end -= 1
            max_idx -= 1
            
        return pancake_flips
            
        