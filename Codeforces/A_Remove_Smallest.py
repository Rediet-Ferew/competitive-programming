test_cases = int(input())

for _ in range(test_cases):
    
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    
    if n == 1:
        print('YES')
        continue
    
    remaining = n
    idx = 0
    
    while idx < n - 1:
        
        nxt = idx + 1
        if nums[nxt] - nums[idx] < 2:
            remaining -= 1
            
        idx += 1
                
    if remaining == 1:
        print('YES')
    else:
        print('NO')
