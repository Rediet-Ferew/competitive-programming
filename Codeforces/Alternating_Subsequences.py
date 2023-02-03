test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    nums = list(map(int, input().split()))
    max_sum = 0
    idx = 0
    
    while idx < n:
        
        if nums[idx] < 0:
            curr_max = float('-inf')
            
            while idx < n and nums[idx] < 0:
                curr_max = max(curr_max, nums[idx])
                idx += 1
            max_sum += curr_max
            
        elif nums[idx] > 0:
            curr_max = float('-inf')
            
            while idx < n and nums[idx] > 0:
                curr_max = max(curr_max, nums[idx])
                idx += 1
            max_sum += curr_max
        
    print(max_sum)
