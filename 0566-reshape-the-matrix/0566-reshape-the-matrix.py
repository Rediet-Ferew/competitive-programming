class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rowLen = len(mat)
        colLen = len(mat[0])
        n_elements = rowLen * colLen
        r_elements = r * c
        
        if n_elements > r_elements:
            return mat
        
        if n_elements < r_elements:
            r = min(r, rowLen)
            c  = min(c, colLen)
        
        #create the r x c matrix
        reshaped = [[0 for _i in range(c)] for _ in range(r)]
        n = ((r - 1) * c) + (c - 1)
        
        #place the numbers based on the unique numbers
        for idx in range(n + 1):
            
            row_or =(idx // colLen)
            col_or = (idx % colLen)
            row =(idx // c)
            col = (idx % c)
            
            reshaped[row][col] = mat[row_or][col_or]
        
        return reshaped
                
                