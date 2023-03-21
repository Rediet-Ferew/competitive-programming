class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [["."] * n for i in range(n)]
        count = 0
    
        def helper( grid, row, n):
            nonlocal count
            
            if row >= n:
                count += 1
                return

            for i in range(n):
                if self.upper(row, i, grid) and self.leftdia(row, i, grid) and self.rightdia(row, i, grid, n):
                    grid[row][i] = "Q"
                    helper(grid, row + 1,n)
                    grid[row][i] = "."
                    
        helper(grid, 0, n)
        return count
                    

    def upper(self, row, col, grid):
        for i in range(row, -1, -1):
            if grid[i][col] != ".":
                return False
            
        return True
    
    def leftdia(self, row, col, grid):
        if row < 0:
            return True
        
        if col < 0 :
            return True
        
        if grid[row][col] != ".":
            return False
        
        return self.leftdia(row - 1, col - 1, grid)
            
    
    def rightdia(self, row, col, grid, n):
        if col >= n:
            return True
        if row < 0:
            return True
        
        if grid[row][col] != ".":
            return False
        
        return self.rightdia(row - 1, col + 1, grid, n)