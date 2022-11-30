class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # a decreasing stack
        min_val = nums[0] #keeping the minimum ith value because we want to minimize it
        for i in range(1, len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
                
            if stack and nums[i] > stack[-1][1]:
                return True
            stack.append((nums[i], min_val))
            min_val = min(min_val, nums[i])
        return False