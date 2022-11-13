class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        k = 0  
        l r
        [1,1,1,0,0,0,1,1,1,1,0]
         l
                   r
        """
         #sliding window
        ans = 0
        n = len(nums)
        left = k
        prev = 0
        for i in range(n):
            if nums[i] == 1:
                # no need to flip
                continue
            else:
                # check if we can flip 
                if left > 0:
                    left -= 1
                    continue
                else:
                    # we cannot flip so sliding window is stopped
                    if i - prev > ans : ans = i - prev
                    # now sliding window will shrink
                    while prev < i and nums[prev] != 0:
                        prev += 1
                    prev += 1
        if n - prev > ans : ans = n - prev
        return ans