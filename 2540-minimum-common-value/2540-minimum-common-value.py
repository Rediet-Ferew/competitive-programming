class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        nums1.sort()
        nums2.sort()
        min_val = -1
        pt1 = 0
        pt2 = 0
        while pt1 < n1 and pt2 < n2:
            if nums1[pt1] == nums2[pt2]:
                min_val = nums1[pt1]
                break
            elif nums1[pt1] < nums2[pt2]:
                pt1 += 1
            else:
                pt2 += 1
        return min_val