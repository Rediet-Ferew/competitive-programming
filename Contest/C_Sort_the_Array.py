
n = int(input())

nums = list(map(int, input().split()))
def sorting(nums):
    if nums == sorted(nums):
        print("yes")
        print(str(1) + ' ' + str(1))
        return
    if n == 1:
        print("yes")
        print(str(1) + ' ' + str(1))
        return
    if n == 2:
        if sorted(nums) == nums:
            print("yes")
            print(str(1) + ' ' + str(1))
            
        else:
            print("yes")
            print(str(1) + ' ' + str(2))
        return
    idx = 0
    start = 0
    end = 0
    while idx < n - 1:
        if nums[idx + 1] < nums[idx]:
            start = idx
            while idx < n - 1 and nums[idx + 1] < nums[idx]:
                idx += 1
            end = idx
            
        else:
            idx += 1
            continue
            
            
           
    l = start
    r = end
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    
    if nums == sorted(nums):
        print("yes")
        print(str(start + 1) + ' ' + str(end + 1))
    else:
        print("no")
    return
            

    
sorting(nums)
