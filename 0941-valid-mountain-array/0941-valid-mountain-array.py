class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #find the index of the maximum value
        n = len(arr)
        max_num = max(arr)
        max_idx = 0
        
        for idx in range(n):
            if arr[idx] == max_num:
                max_idx = idx
                break
        
        #the index cannot be an edge index
        if max_idx == 0 or max_idx == n - 1:
            return False
        
        left = max_idx
        right = max_idx
        
        #left part check
        while left > 0:
            if arr[left - 1] >= arr[left]:
                return False
            left -= 1
        
        #right part check
        while right < n - 1:
            if arr[right + 1] >= arr[right]:
                return False
            right += 1
        
        return True