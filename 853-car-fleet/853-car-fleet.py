class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        for i in range(len(position)):
            posSpeed.append([position[i], speed[i]])
        posSpeed = sorted(posSpeed)
        stack = []
        for p, s in posSpeed[:: -1]:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)