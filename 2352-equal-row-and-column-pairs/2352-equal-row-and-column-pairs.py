class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        size = len(grid)
        
        # visited = set()
        transpose = []
        for _ in range(size):
            transpose.append([0]*size)
        
        for r in range(size):
            for c in range(size):
                
                transpose[c][r] = grid[r][c]
        
        equal_pairs = 0
        
        for i in range(size):
            for j in range(size):
                if grid[i] == transpose[j]:
                    equal_pairs += 1
        
        return equal_pairs