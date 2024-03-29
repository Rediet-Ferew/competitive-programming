class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        dp = [0] * (n + 1)
        max_len = 0
        for i in range(len(nums1)):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[j + 1] = 1 + dp[j]
                else:
                    dp[j + 1] = 0
                max_len = max(dp[j+1], max_len)
        return max_len
                    
                