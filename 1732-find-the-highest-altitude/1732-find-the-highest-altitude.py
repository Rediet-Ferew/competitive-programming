class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total, max_height = 0, 0
        for num in gain:
            total += num
            max_height = max(max_height, total)
        return max_height