class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        current_water = 0
        max_water = 0
        while start < end:
            if height[start] > height[end]:
                min_height = min(height[start], height[end])
                current_water = min_height * (end - start)
                end -= 1
            else:
                min_height = min(height[start], height[end])
                current_water = min_height * (end - start)
                start += 1
            max_water = max(max_water, current_water)
        return max_water
        
                