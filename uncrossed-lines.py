class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        @cache
        def dp(i, j, cnt):
            if i >= n1 or j >= n2:
                return cnt
            min_cnt = float("-inf")
            if nums1[i] == nums2[j]:
                min_cnt = max(min_cnt, dp(i + 1, j + 1, cnt + 1))
            else:
                min_cnt = max(dp(i + 1, j, cnt), dp(i, j + 1, cnt))
            
            return min_cnt
        return dp(0, 0, 0)