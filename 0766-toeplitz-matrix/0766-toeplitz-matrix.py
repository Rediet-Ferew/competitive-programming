class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        nums_set = collections.defaultdict(set)
        
        for r in range(rowLen):
            
            for c in range(colLen):
                diff = c - r
                nums_set[diff].add(matrix[r][c])
        
        for key, val in nums_set.items():
            
            if len(val) > 1:
                return False
        return True
                