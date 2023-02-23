class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rowLen = len(self.matrix)
        colLen = len(self.matrix[0])
        self.pre_matrix = []
        
        for i in range(rowLen + 1):
            row = []
            for j in range(colLen + 1):
                row.append(0)
            self.pre_matrix.append(row)
        for r in range(rowLen):
            for c in range(colLen):
                _sum = self.pre_matrix [r][c+1] + self.pre_matrix [r+1][c] + self.matrix[r][c] - self.pre_matrix [r][c]
                self.pre_matrix [r+1][c+1] = _sum
                
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        crude = self.pre_matrix[row2+1][col2+1]
        total = crude - self.pre_matrix[row2+1][col1]-self.pre_matrix[row1][col2+1]+self.pre_matrix[row1][col1]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)