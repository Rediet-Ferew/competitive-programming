class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        #find the n - k index
        
        if k == 0:
            return
        
        if k > n:
            k = k % n
            
        idx = n - k
        nums[:idx] = nums[:idx][::-1]
        nums[idx:] = nums[idx:][::-1]
            
        left = 0
        right = n - 1
        
        while left <= right and k > 0:
            
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            k -= 1
            
        nums[left:right + 1] = nums[left:right + 1][::-1]