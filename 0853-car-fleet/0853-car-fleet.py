class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[p, s] for p, s in zip(position, speed)]
        pos_speed = sorted(pos_speed)[::-1]
        stack = []
        for p, v in pos_speed:
            t = (target - p) / v
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)