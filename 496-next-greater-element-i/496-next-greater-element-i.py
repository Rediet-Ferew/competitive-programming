class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = {num:i for i, num in enumerate(nums1)}
        print(indices)
        stack = [-1] * len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in indices:
                continue
            for j in range(i + 1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        stack[indices[nums2[i]]] = nums2[j]
                        break
        return stack