# import sys
# input = sys.stdin.readline

test_cases = int(input())


for _ in range(test_cases):
    n = int(input())
    matrix = []
    
    for _i in range(n):
        row = list(map(int,input()))
        matrix.append(row)
        
    visited = set()
    min_operations = 0
    
    for r in range(n):
        for c in range(n):
            
            """
            x, y -> y, -x
            x, y -> -x, -y
            x, y ->  -y, x
            for the negatives make n - (x or y) - 1
            """
            
            counts = {
                0 : 0,
                1 : 0
            }
            if (r, c) not in visited:
                #0
                num = matrix[r][c]
                counts[num] += 1
                visited.add((r, c))
                #90
                num_90 = matrix[c][n - r - 1]
                counts[num_90] += 1
                visited.add((c, n - r - 1))
                #180
                num_180 = matrix[n - r - 1][n - c - 1]
                counts[num_180] += 1
                visited.add((n - r - 1, n - c - 1))
                #270
                num_270 = matrix[n - c - 1][r]
                counts[num_270] += 1
                visited.add((n - c - 1, r))
                #find min value to flip
                min_val = min(counts[0], counts[1])
                
                min_operations += min_val
                
    print(min_operations)
            
