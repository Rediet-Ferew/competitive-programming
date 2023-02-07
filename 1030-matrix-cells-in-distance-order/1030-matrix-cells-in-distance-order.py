class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        
        dis = []
        
        for r in range(rows):
            for c in range(cols):
            
                distance = abs(rCenter - r) + abs(cCenter - c)

                dis.append([distance, [r, c]])
        dis.sort()
        
        ans = []
        for i, v in enumerate(dis):
            ans.append(v[1])
        return ans