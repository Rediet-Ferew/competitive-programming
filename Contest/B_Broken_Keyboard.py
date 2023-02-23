test_cases = int(input())

for _ in range(test_cases):
    s = input()
    s_l = list(s)
    n = len(s_l)
    
    idx = 0
    res = []
    while idx < n - 1:
        if s_l[idx] == s[idx + 1]:
            idx += 2
        else:
            res.append(s_l[idx])
            idx += 1
    if idx == n - 1:
        res.append(s_l[n - 1])
        
    res = list(set(res))
    res.sort()
    print("".join(res))
