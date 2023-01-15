class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        #calculate the unique num fo this index
        n = ((rowLen - 1) * colLen) + (colLen - 1)
        
        for idx in range(n + 1):
            row = idx // colLen
            col = idx % colLen
            if matrix[row][col] == target:
                return True
        return False