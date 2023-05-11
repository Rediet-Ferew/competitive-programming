class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        visited = set()
        v = set()
        def isInBound(row, col):
            if row >= 0 and row < rowLen and col >= 0 and col < colLen and grid[row][col] != 0 and (row, col) not in visited:
                return True
            return False
        
        def dfs(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if not isInBound(r, c):
                return []
            
            visited.add((r, c))
            cnt = [(r, c)]
            for row_change, col_change in directions:
                new_row = r + row_change
                new_col = c + col_change

                cnt.extend(dfs(new_row, new_col))
                
            
            return cnt
        
        islands = []
        for r in range(rowLen):
            for c in range(colLen):
                max_area = dfs(r, c)
                
                if max_area:
                    islands.append(set(max_area))
        def isBound(row, col):
            if row >= 0 and row < rowLen and col >= 0 and col < colLen and (row, col) not in v:
                return True
            return False
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = collections.deque(islands[0])
        
        level = 0
        min_level = float("inf")
        while q:

            cur_len = len(q)
            for _ in range(cur_len):
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if isBound(new_r, new_c) and (new_r, new_c) in islands[1] and (new_r, new_c) not in islands[0]:
                        # level += 1
                        min_level = min(min_level, level)
                        continue
                    if isBound(new_r, new_c) and (new_r, new_c) not in islands[0] and grid[new_r][new_c] == 0:
                        v.add((new_r, new_c))
                        q.append((new_r, new_c))
            level += 1
            
        
        return min_level