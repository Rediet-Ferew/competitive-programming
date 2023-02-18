class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        cnt = 0
        for idx in range(len(heights)):
            if heights[idx] != expected[idx]:
                cnt += 1
        return cnt