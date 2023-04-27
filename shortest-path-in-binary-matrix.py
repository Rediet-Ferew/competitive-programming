class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def isInBound(row, col):
            if row >= 0 and row < rowLen and col >= 0 and col < colLen and grid[row][col] == 0 and (row, col) not in visited:
                return True
            return False

        rowLen = len(grid)
        colLen = len(grid[0])

        target = (rowLen - 1, colLen - 1)

        if grid[0][0] == 1 or grid[rowLen - 1][colLen - 1] == 1:
            return -1

        if target == (0, 0):
            return 1

        q = collections.deque()
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        level = 1
        
        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                val = q.popleft()
              
                for r_ch, c_ch in directions:
                    
                    n_r = val[0] + r_ch
                    n_c = val[1] + c_ch
                    if isInBound(n_r, n_c):
                        print(n_r, n_c)

                        if (n_r, n_c) == target:
                            
                            level += 1
                            return level
                        q.append((n_r, n_c))
                        visited.add((n_r, n_c))
                 
            level += 1
        return -1