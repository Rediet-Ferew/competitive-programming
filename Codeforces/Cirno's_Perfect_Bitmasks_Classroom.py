import math
t = int(input())

for _ in range(t):

    n = int(input())
    log_val = math.floor(math.log2(n))
    ans = 0
    b_rep = bin(n)
    b_rep = b_rep[2:]
    # print(b_rep)
    i = 0
    l = len(b_rep)
    
    #first one
    for s in b_rep[::-1]:
        if s == '0':
            i += 1
        else:
            break
    # print(i)
    j = 0
    #first zero
    for p in b_rep[::-1]:
        if p == '1':
            j += 1
        else:
            break
    
    # print(j)
    num = 1 << i
    # print(bin(num))
    if (2 ** log_val) == n:
        num |= (1 << j)
    print(num)
    
