class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        column = len(matrix[0])
        self.numMatrix = [[0] * (column + 1) for i in range(row + 1)]
        for i in range(row):
            prefixSum = 0
            for j in range(column):
                prefixSum += matrix[i][j]
                above = self.numMatrix[i][j+1]
                self.numMatrix[i+1][j + 1] = prefixSum + above
        print(self.numMatrix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summation =  self.numMatrix[row2 + 1][col2 + 1]  - self.numMatrix[row1][col2 + 1]  - self.numMatrix[row2 + 1][col1] + + self.numMatrix[row1][col1] 
        return summation

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)