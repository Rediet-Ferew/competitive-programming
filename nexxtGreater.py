class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        check = False
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and j < (len(nums2) - 1):
                    for k in (j + 1, len(nums2) - 1):
                        if nums2[k] > nums2[j]:
                            answer.append(nums2[k])
                            check = True
                            break
                        else:
                            continue
                    if not check:
                        answer.append(-1)
                elif nums1[i] == nums2[j] and j == (len(nums2) - 1):
                    answer.append(-1)
        return answer