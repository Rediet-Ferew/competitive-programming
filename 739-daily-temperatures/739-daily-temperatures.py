class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        days = [0] * n
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][-1]:
                i, t = stack.pop()
                days[i] = idx - i
            stack.append([idx, temp])
        # print(days)
        return days
                