class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = set()
        rowLen = len(matrix)
        colLen = len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0 :
                    zeros.add((r,c))
        for pts in list(zeros):
            r, c = pts
            for i in range(colLen):
                matrix[r][i] = 0
            for j in range(rowLen):
                matrix[j][c] = 0