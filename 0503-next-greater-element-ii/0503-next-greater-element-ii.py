class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []
        for _ in range(2):
            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    idx = stack.pop()
                    result[idx] = nums[i]
                stack.append(i)
        return result
        