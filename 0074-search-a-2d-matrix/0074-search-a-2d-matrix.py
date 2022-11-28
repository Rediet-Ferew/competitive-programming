class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        for r in range(rowLen):
            left = 0
            right = colLen - 1
            while left <= right:
                mid =(left+right)//2
                if matrix[r][mid] == target:
                    return True
                elif matrix[r][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False