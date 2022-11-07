class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rlen = len(grid)
        clen = len(grid[0])
        land_set = set()
        def count_land(r : int, c : int):
            if r >= rlen or c >= clen or r < 0 or c < 0 or grid[r][c] == 0 or (r,c) in land_set:
                return 0
            land_set.add((r, c))
            return (
            1 + count_land(r - 1, c) +
            count_land(r + 1, c) +
            count_land(r, c - 1) +
            count_land(r, c + 1))
        max_area = 0
        for r in range(rlen):
            for c in range(clen):
                max_area = max(max_area,count_land(r, c))
        return max_area
                