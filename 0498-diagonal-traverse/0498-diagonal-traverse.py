class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rowLen = len(mat)
        colLen = len(mat[0])
        diagonals = collections.defaultdict(list)
        
        for r in range(rowLen):
            for c in range(colLen):
                diagonals[r+c].append(mat[r][c])
        

        res = []
        for key, val in diagonals.items():
            
            if key % 2 == 0:
                res.extend(val[::-1])
            else:
                res.extend(val)
        
        return res