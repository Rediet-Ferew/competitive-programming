class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rowLen = len(board)
        colLen = len(board[0])
        
        def isInBound(row, col):

            if row >= 0 and row < rowLen and col >= 0 and col < colLen:
                return True
            return False

        def countMines(r, c):
            cnt = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1,-1),(1,-1),(-1,1)]
           
            for new_row, new_col in directions:
                row_changed = r + new_row
                col_changed = c + new_col
                if isInBound(row_changed, col_changed) and board[row_changed][col_changed] == 'M':
                    cnt += 1
            return cnt

        def dfs(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1,-1),(1,-1),(-1,1)]
            
            if not isInBound(r, c) or board[r][c] != 'E':
                return 
            cnt = countMines(r, c)
            if cnt:
                board[r][c] = str(cnt)
            else:
                board[r][c] = 'B'
                for new_row, new_col in directions:
                    row_changed = r + new_row
                    col_changed = c + new_col
                    
                    dfs(row_changed, col_changed)
            
        if board[click[0]][click[1]] =='M':
            board[click[0]][click[1]] = 'X'
            return board
        else:
            dfs(click[0], click[1])
            return board