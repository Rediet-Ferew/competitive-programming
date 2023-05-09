class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rowLen = len(maze)
        colLen = len(maze[0])
        
        
        visited = set()
        def isInBound(row, col):
            if row >= 0 and row < rowLen and col >= 0 and col < colLen and (row, col) not in visited:
                return True
            return False
        def isValid(row, col):
            if (col == colLen - 1 or col == 0 or row == 0 or row == rowLen - 1) and (row, col) != (entrance[0], entrance[1]):
                return True
            return False
        q = collections.deque()
        q.append((entrance[0], entrance[1]))
        visited.add((entrance[0], entrance[1]))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        level = 0
        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                ent = q.popleft()
                for r_ch, c_ch in directions:
                    new_r = r_ch + ent[0]
                    new_c = c_ch + ent[1]
                    if isInBound(new_r, new_c) and maze[new_r][new_c] == '.'and isValid(new_r, new_c):
                        level += 1
                        return level
                    
                    if isInBound(new_r, new_c) and maze[new_r][new_c] == ".":
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
            level += 1
        return -1