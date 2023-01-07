class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        counter = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] < 0:
                    counter += 1
        return counter