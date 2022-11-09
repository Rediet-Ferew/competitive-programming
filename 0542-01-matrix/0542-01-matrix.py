class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        q = deque()
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
        neighbor = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x,y = q.popleft()
            for cell in neighbor:
                new_x, new_y = x + cell[0] , y + cell[1]
                if new_x >= 0 and new_y >= 0 and new_x <= len(mat) -1 and new_y <= len(mat[0])-1 and (new_x, new_y) not in visited:
                    mat[new_x][new_y] = mat[x][y] + 1
                    visited.add((new_x, new_y))
                    q.append((new_x, new_y))
        return mat