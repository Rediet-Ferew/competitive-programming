class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        print(merged)
        mid = 0
        median = 0
        n = len(merged)
        half = n//2
        if len(merged) %2 == 0:
            mid = merged[half] + merged[half - 1]
            median = mid/2
        else:
            mid = merged[half]
            median = float(mid)
        return median
#         from statistics import median
#         if not nums1:
#             return statistics.median(nums2)
#         elif not nums2:
#             return statistics.median(nums1)
            
#         mid1 = statistics.median(nums1)
#         mid2 = statistics.median(nums2)
#         mid = (mid1 + mid2)/2
#         return mid