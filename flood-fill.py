class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rowLen = len(image)
        colLen = len(image[0])
        visited = set()
        curr_color = image[sr][sc]
        
        def isInBound(row, col):
            if row >= 0 and row < rowLen and col >= 0 and col < colLen:
                return True
            return False
        
        def dfs(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            if not isInBound(r, c):
                return 
            else:
                visited.add((r, c))

                for row_change, col_change in directions:
                    
                    new_row = r + row_change
                    new_col = c + col_change
                    if isInBound(new_row, new_col) and (new_row, new_col) not in visited:
                        if image[new_row][new_col] == curr_color:
                            image[new_row][new_col] = color
                            dfs(new_row, new_col)
        dfs(sr, sc)
        image[sr][sc] = color
        return image