class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rowLen = len(grid)
        colLen = len(grid[0])
        
        #create maxlocal matrix
        max_local = [[0 for _i in range(colLen - 2)] for _ in range(rowLen - 2)]
        r = len(max_local)
        c = len(max_local[0])
        #calculate the unique number
        n = ((r - 1) * c) + (c - 1)
        
        
        for idx in range(n + 1):
            
            row =(idx // c)
            col = (idx % c)
            max_num = float('-inf')
            
            #calculate the maximum number for each 3 x 3 contiguous matrix
            for i in range(row, (row + 3)):
                for j in range(col, (col + 3)):
                    
                    max_num = max(max_num, grid[i][j])
                    
            max_local[row][col] = max_num
        
        return max_local
                