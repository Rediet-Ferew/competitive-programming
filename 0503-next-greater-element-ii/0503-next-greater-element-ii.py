class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        greater = [-1] * len(nums)
        for idx, num in enumerate(nums):
            while stack and num > stack[-1][0]:
                n, i = stack.pop()
                greater[i] = num
            stack.append([num, idx])
        
        for idx, num in enumerate(nums):
            while stack and num > stack[-1][0]:
                n, i = stack.pop()
                greater[i] = num
            stack.append([num, idx])
        return greater