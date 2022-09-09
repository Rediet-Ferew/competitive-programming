class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        new = []
        if m == 1:
            return matrix[0][0]
        for i in range(n):
            for j in range(m):
                new.append(matrix[i][j])
        new =sorted(new)
        return new[k - 1]
                