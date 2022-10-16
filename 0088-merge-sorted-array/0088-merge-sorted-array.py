class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = n + m - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[end] = nums1[m - 1]
                m -= 1
            else:
                nums1[end] = nums2[n - 1]
                n -= 1
            end -= 1
        while n > 0:
            nums1[end] = nums2[n - 1]
            n = n - 1
            end = end - 1
        # if nums1 and nums2:
        #     if m == 1 and n == 1:
        #         nums1[0] = nums2[0]
        #     for idx in range(m, m + n):
        #         nums1[idx] = nums2.pop()
        # # if m == 0:
        # #     for i in range(n):
        # #         nums1[i] = nums2.pop()
        # nums1.sort()
       
            