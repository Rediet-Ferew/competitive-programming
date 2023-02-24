class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_map = {}
        for num in nums1:
            greater_map[num] = -1
            
        
        stack = []
        for i in range(len(nums2)):
            if not stack or stack[-1] >= nums2[i]:
                stack.append(nums2[i])
            else:
                while stack and stack[-1] < nums2[i]:
                    temp = stack.pop()
                    if temp in greater_map:
                        greater_map[temp] = nums2[i]
                    
                stack.append(nums2[i])

                        
        return greater_map.values()