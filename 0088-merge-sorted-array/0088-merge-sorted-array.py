class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #check for the max numbers at the end of the two arrays
        #place the max at the end
        
        end = n + m - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[end] = nums1[m - 1]
                m -= 1
            else:
                nums1[end] = nums2[n - 1]
                n -= 1
            end -= 1
        #if remaining on the right side make them fit the first num
        while n > 0:
            nums1[end] = nums2[n - 1]
            n = n - 1
            end = end - 1