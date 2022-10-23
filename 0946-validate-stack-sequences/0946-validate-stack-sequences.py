class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(pushed)
        j = 0
        for i in range(n):
            stack.append(pushed[i])
            while stack and popped[j] == stack[-1] and i < n:
                j += 1
                stack.pop()
        return len(stack) == 0