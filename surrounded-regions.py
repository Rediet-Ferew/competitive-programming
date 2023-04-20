class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowLen = len(board)
        colLen = len(board[0])
        visited = set()
        def isInBound(row, col):
            if row >= 0 and row < rowLen and col >= 0 and col < colLen and board[row][col] == 'O' and (row, col) not in visited:
                return True
            return False
        
        def dfs(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if not isInBound(r, c):
                return
            visited.add((r, c))
            for row_change, col_change in directions:
                new_row = r + row_change
                new_col = c + col_change
                dfs(new_row, new_col)
        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == 'O' and (r == 0 or c == 0 or r == rowLen -1 or c == colLen - 1):
                    dfs(r, c)
        for i in range(rowLen):
            for j in range(colLen):
                if (i, j) in visited:
                    
                    board[i][j] = 'O'
                
                elif (i, j) not in visited and board[i][j] =='O':
                    board[i][j] = 'X'