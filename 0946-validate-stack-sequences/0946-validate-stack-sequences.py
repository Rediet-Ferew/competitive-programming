class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped = popped[::-1]
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
        return len(stack) == 0
                