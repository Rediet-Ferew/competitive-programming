class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            astr = asteroids[i]
            while stack and  (stack[-1] > 0 and astr < 0):
                abs2 = abs(astr)
                if stack[-1] > abs2:
                    astr = 0
                elif stack[-1] < abs2:
                    stack.pop()
                else:
                    astr = 0
                    stack.pop()
            if astr != 0:
                stack.append(astr)
        return stack
                