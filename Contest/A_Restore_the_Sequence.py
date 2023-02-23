test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    nums = list(map(int, input().split()))
    
    left = 0
    right = n - 1
    ans = []
    
    while left <= right:
        if left == right and n % 2 != 0:
            ans.append(nums[left])
            break
        ans.append(nums[left])
        left += 1
        ans.append(nums[right])
        right -= 1
        
        
    print(*ans)
