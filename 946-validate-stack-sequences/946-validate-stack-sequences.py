class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(pushed)
        j = 0
        for i in range(n):
            # if popped[i] == stack[-1] and stack:
            #     stack.pop()
            # else:
            stack.append(pushed[i])
            while stack and popped[j] == stack[-1] and i < n:
                j += 1
                stack.pop()
        print(stack)
        
                
        if stack:
            return False
        else:
            return True