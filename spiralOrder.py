class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ordered = []
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(n - 1):
            ordered.append(matrix[0][i])
        for i in range(m):
            ordered.append(matrix[i][-1])
        for i in range(n - 2, -1, -1):
            ordered.append(matrix[-1][i])
        for i in range(1, m - 1):
            for j in range(0, n - 1):
                ordered.append(matrix[i][j])
        return ordered