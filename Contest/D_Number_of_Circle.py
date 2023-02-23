n = int(input())

nums = list(map(int, input().split()))
nums.sort()

        
def checker(nums):
    if nums[n - 3] + nums[n - 2] <= nums[n - 1]:
        print('NO')
        return
    else:
        nums[n - 2], nums[n - 1] = nums[n - 1], nums[n - 2]
        print('YES')
        print(*nums)
        return      
    
checker(nums)
        
