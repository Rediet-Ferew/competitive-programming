class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        num = (cols - 1) * cols + (rows - 1)
        
        dis = []
        
        for r in range(rows):
            for c in range(cols):
            
                distance = abs(rCenter - r) + abs(cCenter - c)

                dis.append([distance, [r, c]])
        res = []
        for key, val in dis:
            res.append([key, val])
        res.sort()
        ans = []
        for i, v in enumerate(res):
            ans.append(v[1])
        return ans