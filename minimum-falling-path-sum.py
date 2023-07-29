class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        l=len(matrix)
       
        for i in range(1,l):
           
            matrix[i][0]+=min(matrix[i-1][0:2])
            for j in range(1,l):
                matrix[i][j]+=min(matrix[i-1][j-1:j+2])
       
        return min(matrix[l-1])