class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        pairs = [(num, idx) for idx, num in enumerate(temperatures)]
        
        stack = []
        days = [0] * n
        for i in range(n):
            if not stack or stack[-1][0] >= pairs[i][0]:
                stack.append(pairs[i])
            else:
                while stack and stack[-1][0] < pairs[i][0]:
                    num, idx = stack.pop()
                    days[idx] = i - idx
                stack.append(pairs[i])
        
        return days
                
        