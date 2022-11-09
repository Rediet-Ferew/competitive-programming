class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        count = []
        fresh_set = set()
        rotten_set = set()
        rlen = len(grid)
        clen = len(grid[0])
        for r in range(rlen):
            for c in range(clen):
                if grid[r][c] == 2:
                    rotten_set.add((r,c))
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_set.add((r,c))
        n = len(fresh_set)
        minutes = 0
        neighbor = [(1,0),(-1,0),(0,1),(0,-1)]
        while q and n > 0:
            minutes += 1
            for i in range(len(q)):   ## working on the current level of the matrix
                x, y = q.popleft()
                for cell in neighbor:
                    nx, ny = x + cell[0], y + cell[1]
                    if nx >= 0 and nx <= rlen - 1 and ny >=0 and ny<=clen-1 and (nx, ny) not in rotten_set and (nx, ny) in fresh_set:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        rotten_set.add((nx, ny))
                        fresh_set.remove((nx,ny))
                        n -= 1
        if len(fresh_set) != 0:
            return -1
        return minutes
        # print("########")
            
                
                    
            