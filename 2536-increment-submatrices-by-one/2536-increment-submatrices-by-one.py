class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        mat = [[0] * n for _ in range(n)]
    
        for i in range(len(queries)):
            row1, col1, row2, col2 = queries[i]
            for j in range(row1, row2 + 1):
                mat[j][col1] += 1
                if col2 + 1 < n:
                    mat[j][col2 + 1] -= 1
                    
        for row in range(n):
            for col in range(1, n):
                mat[row][col] += mat[row][col - 1]
                
        return mat