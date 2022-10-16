class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # left = 0
        if n == len(set(nums)):
            return False
        
        for i in range(n - 1):
            right = i + 1
            while right < n:
                if nums[right] == nums[i]:
                    if abs(right - i) <= k:
                        return True
                    # break
                right += 1
        # if arr:
        #     return True
        # else:
        return False
        
            