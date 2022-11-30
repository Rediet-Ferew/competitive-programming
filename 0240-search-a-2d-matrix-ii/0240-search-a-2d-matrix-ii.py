class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        for i in range(rowLen):
            l = 0
            r = colLen - 1
            while l <= r:
                m = (l+r)//2
                if matrix[i][m] > target:
                    r = m - 1
                elif matrix[i][m] < target:
                    l = m+1
                else:
                    return True
        return False