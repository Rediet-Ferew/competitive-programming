class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLen, colLen = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for x, y in directions:
                    new_x, new_y = row+x, col+y
                    if new_x >= 0 and new_y >= 0 and new_x < rowLen and new_y < colLen and grid[new_x][new_y] =="1" and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        q.append((new_x, new_y))
                
                    
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
                    
            