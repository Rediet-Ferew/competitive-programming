class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
#         n = len(board)
#         cols = [[]]*n
#         #row checking
#         for r in range(9):
#             templ = []
#             for ch_n in board[r]:
#                 if ch_n != "." and ch_n not in ["1","2","3","4","5","6","7","8","9"]:
#                     return False
#                 if ch_n != ".":
#                     templ.append(ch_n)
#             if len(templ) != len(set(templ)):
#                 return False
#         #column matrix
#         for i in range(n):
#             temp  =[]
#             for c in range(n):
#                 temp.append(board[c][i])
#             cols[i] = temp
#         # #column checking
#         for c in cols:
#             temp_l = []
#             for ch in c:
#                 if ch != "." and ch not in ["1","2","3","4","5","6","7","8","9"]:
#                     return False
#                 if ch != ".":
#                     temp_l.append(ch)
#             if len(temp_l) != len(set(temp_l)):
#                 return False
        
        # 3x3 boxes checking
        squares = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in squares[(r//3, c//3)]) or (board[r][c] in rows[r]) or (board[r][c] in columns[c]):
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True