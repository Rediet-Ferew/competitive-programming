class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_total = float("-inf")
        l = 0
        r = 2
        while r < row:
            total = [0]*3
            total[0] = sum(grid[l][:3])
            total[1] = grid[l+1][1]
            total[2] = sum(grid[r][:3])
            max_total = max(sum(total), max_total)
            left = 0
            right = 2
            while right < col-1:
                total[0] -= grid[l][left]
                total[0] += grid[l][right+1]
                total[1] = grid[l+1][right]
                total[2] -= grid[l+2][left]
                total[2] += grid[l+2][right+1]
                max_total = max(sum(total), max_total)
                left += 1
                right += 1
            max_total = max(sum(total), max_total)
            l += 1
            r += 1
        return max_total
        