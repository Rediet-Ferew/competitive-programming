class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #store the last element as the current max
        curr_max = arr[-1]
        arr[-1] = -1        
        n = len(arr)
        
        #update the current max from the end
        for i in range(n-2, -1, -1):
            
            curr_num = arr[i]
            arr[i] = curr_max
            
            if curr_num > curr_max:
                curr_max = curr_num
                
        return arr