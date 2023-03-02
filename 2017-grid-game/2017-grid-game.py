class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        top_sum = sum(grid[0])
        bottom_sum = 0
        robot_max = float('inf')
        
        idx = 0
        for i in range(n):
            
            top = grid[0][idx]
            bottom = grid[1][idx]
            
            top_sum -= top
            curr_max = max(top_sum, bottom_sum)
            bottom_sum += bottom
            
            robot_max = min(curr_max, robot_max)
            idx += 1
            
        return robot_max