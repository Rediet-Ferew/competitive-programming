class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowLen = len(grid)
        colLen = len(grid[0])
        row_count = [0]*rowLen
        col_count = [0]*colLen
        
        #finding the number of ones for each column and row
        for r in range(rowLen):
            for c in range(colLen):
                
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1
                    
        #calculate the diff value and update the value in place
        for r in range(rowLen):
            for c in range(colLen):
                
                diff = row_count[r] + col_count[c] - ((rowLen - row_count[r]) + (colLen - col_count[c]))
                grid[r][c] = diff
                
        return grid