
test_cases = int(input())

for _ in range(test_cases):
    input('\n')
    matrix = []
    for i in range(8):
        row = list(input())
        matrix.append(row)

    diff = set()
    pre_sum = set()
    
    for r in range(8):
        temp = []
        for c in range(8):
            char = matrix[r][c]
            
            if char == '#':
                temp.append([c, r])
                temp.sort()
        if len(temp) == 2:
            t = temp[1][0] + temp[1][1]
            m = temp[0][1] - temp[0][0]
            pre_sum.add(t)
            diff.add(m)
            break
    
          
    returned = []
    def evaluater():
        for k in range(8):
            for l in range(8):
                
                ch = matrix[k][l]
                d = k - l
                s = k + l
                if ch == '#' and (d in diff) and(s in pre_sum):
                    returned.append(k + 1)
                    returned.append(l + 1)
                    return returned
    ans = evaluater()
    print(*ans, end = '')
        
