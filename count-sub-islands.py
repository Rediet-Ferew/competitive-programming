class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rowLen = len(grid1)
        colLen = len(grid1[0])
        visited = set()
        k = 0
        def isInBound(row, col):
            if row < 0 or row >= rowLen or col < 0 or col >= colLen or grid2[row][col] == 0:
                return False

            return True
        
        def dfs(grid1, grid2, r, c):
            nonlocal k
            visited.add((r, c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if grid1[r][c] != 1:
                k = 1
            
            for row_change, col_change in directions:
                new_row = r + row_change
                new_col = c + col_change
                if isInBound(new_row, new_col) and (new_row, new_col) not in visited:
                    
                    dfs(grid1, grid2, new_row, new_col)
            
                
        cnt = 0
        for r in range(rowLen):
            for c in range(colLen):
                if (r, c) in visited or grid2[r][c] == 0:
                    continue
                dfs(grid1, grid2, r, c)
                if k == 0:
                    cnt += 1
                k = 0
        return cnt