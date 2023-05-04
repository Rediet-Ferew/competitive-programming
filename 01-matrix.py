class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rowLen = len(mat)
        colLen = len(mat[0])
        def isInBound(row, col):
            if row >= 0 and row < rowLen and col >= 0 and col < colLen and (row, col) not in visited:
                return True
            return False
        q = collections.deque()
        visited = set()
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for r in range(rowLen):
            for c in range(colLen):
                if mat[r][c] == 0:
                    q.append([(r, c), 0])
                    visited.add((r,c))
        
        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                node, d = q.popleft()
                
                for r, c in directions:
                    new_r = node[0] + r
                    new_c = node[1] + c
                    if isInBound(new_r, new_c):
                        if mat[new_r][new_c] == 1:
                            q.append([(new_r, new_c), d + 1])
                            mat[new_r][new_c] += (mat[node[0]][node[1]])
                    visited.add((new_r, new_c))
        return mat