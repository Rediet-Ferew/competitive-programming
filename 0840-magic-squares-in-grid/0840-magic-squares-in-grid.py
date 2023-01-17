class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        if rowLen < 3 or colLen < 3:
            return 0
        r = rowLen - 2
        c = colLen - 2
        
        n = ((r - 1) * c) + (c - 1)
        magic_square = 0
        for idx in range(n + 1):
            
            row =(idx // c)
            col = (idx % c)
            row_sum = [] 
            col_sum = [0] * 3
            right_diagonal = 0
            left_diagonal = 0
            sub_grid = []
            
            
            #calculate the maximum number for each 3 x 3 contiguous matrix
            for i in range(row, row + 3):
                temp_s = 0
                for l in range(col, col + 3):
                    temp_s += grid[i][l]
                    if grid[i][l] in range(1, 10):
                        sub_grid.append(grid[i][l])
                row_sum.append(temp_s)
                # row_sum
                # r_sum = sum(grid[i][:row+3])
                # row_sum.append(r_sum)
                
            for j in range(col, col + 3):
                temp_sum = 0
                for k in range(row, row + 3):
                    col_sum[j - col] += grid[k][j]
                    if j - col == k - row:
                        right_diagonal += grid[k][j]
            
                    idx_sum = (j - col) + (k - row)
                    if idx_sum == 2:
                        left_diagonal += grid[k][j]
            # print(row_sum)
            if len(set(sub_grid)) < 9:
                continue
            col_set = []
            if row_sum == col_sum:
                col_set = list(set(col_sum))
            else:
                continue
            if len(col_set) == 1:
                if col_set[0] == left_diagonal == right_diagonal:
                    magic_square += 1
        return magic_square
                
            
                    
            