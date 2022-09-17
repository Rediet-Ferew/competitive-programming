class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        nums1.sort()
        nums2.sort()
        n = len(nums1) if len(nums1) <= len(nums2) else len(nums2)
        nums = nums1 if len(nums1) <= len(nums2) else nums2
        numLong = nums1 if len(nums1) > len(nums2) else nums2
        for i in range(len(nums)):
            if nums[i] in numLong:
                output.append(nums[i])
        return list(set(output))
            