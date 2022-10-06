import numpy as np
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while len(matrix) > 0:
            result += matrix[0]
            matrix = np.transpose(matrix[1:])[::-1].tolist()
        return result