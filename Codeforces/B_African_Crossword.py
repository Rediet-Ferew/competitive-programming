import collections
n, m = map(int, input().split())

board = []

for i in range(n):
    words = list(input())
    board.append(words)

num = ((n - 1) * m) + (m - 1)

row_count = collections.defaultdict(dict)
col_count = collections.defaultdict(dict)

for idx in range(num + 1):
    r = idx // m
    c = idx % m
    letter = board[r][c]
    if letter not in row_count[r]:
        row_count[r][letter] = 1
    else:
        row_count[r][letter] += 1
    if letter not in col_count[c]:
        col_count[c][letter] = 1
    else:
        col_count[c][letter] += 1

ans = ""
for pos in range(num + 1):
    row = pos // m
    col = pos % m
    char = board[row][col] 
    if row_count[row][char] == 1 and col_count[col][char] == 1:
        ans += char
print(ans)
    
        
    
