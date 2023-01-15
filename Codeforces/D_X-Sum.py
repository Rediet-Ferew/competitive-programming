test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())
    matrix = []
    
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
     
    summation = {}
    difference = {}
    max_sum = 0
    
    for r in range(n):
        for c in range(m):
            sm = r + c
            diff = r - c
            num = matrix[r][c]
            
            if sm in summation:
                summation[sm] += num
            else:
                summation[sm] = num
            
            if diff in difference:
                difference[diff] += num
            else:
                difference[diff] = num
            
            
    for i in range(n):
        for j in range(m):
            curr_num = matrix[i][j]
            curr_sm = i + j
            curr_diff = i - j
            total = summation[curr_sm]
            diffr = difference[curr_diff]
            curr_sum = (total + diffr) - curr_num
            max_sum = max(max_sum, curr_sum)
      
    print(max_sum)
