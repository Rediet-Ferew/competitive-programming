class Solution:
    def maxArea(self, height: List[int]) -> int:
        areas = []
        if len(height) == 2:
            return height[1]
        for i in range(2, (len(height))):
            for j in range(1, i):
                areas.append(((i - j) * height[i]))
        return max(areas)
                