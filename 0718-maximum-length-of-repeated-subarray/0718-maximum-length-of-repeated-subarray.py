class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def longestPrefix(arr1: List[int], arr2: List[int]):
            longest = []
            p1 = 0
            p2 = 0
            while arr1 and arr2 and p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] == arr2[p2]:
                    longest.append(arr1[p1])
                    p1 += 1
                    p2 += 1
                else:
                    return len(longest)
            return len(longest)
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
                # temp = longestPrefix(nums1[i:], nums2[j:])
                # dp.append(temp)
        return max_len
                    
                