class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowLen = len(matrix)
        colLen = len(matrix[0])
        visited = set()
        
        for r in range(rowLen):
            for c in range(colLen):
                
                if (r, c) not in visited:
                    
                    r_pos = rowLen - r - 1
                    matrix[r][c], matrix[c][r_pos] = matrix[c][r_pos], matrix[r][c]
                    visited.add((r,c))
                    visited.add((c,r_pos))
                
        # Tansposing
        # for r in range(rowLen):
        #     for c in range(colLen):
        #         if (r,c) not in visited:
        #             matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        #         visited.add((r,c))
        #         visited.add((c,r))
        # # # print(matrix)
        # # #swapping the columns
        # for i in range(rowLen):
        #     l = 0
        #     r = colLen - 1
        #     while l < r:
        #         matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
        #         l += 1
        #         r -= 1
        # print(matrix)