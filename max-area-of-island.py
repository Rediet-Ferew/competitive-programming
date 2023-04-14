class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        visited = set()

        def isInBound(row, col):
            if row >= 0 and row < rowLen and col >= 0 and col < colLen and grid[row][col] != 0 and (row, col) not in visited:
                return True
            return False
        
        def dfs(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if not isInBound(r, c):
                return 0
            
            visited.add((r, c))
            cnt = 1
            for row_change, col_change in directions:
                new_row = r + row_change
                new_col = c + col_change

                cnt += dfs(new_row, new_col)
                
            
            return cnt
        max_area = 0 
        for r in range(rowLen):
            for c in range(colLen):
                max_area = max(max_area, dfs(r, c))
                # print(max_area)
                

        return max_area